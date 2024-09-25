import os
from dotenv import load_dotenv
import streamlit as st
import pdfplumber  # Import pdfplumber
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Load the environment variables
load_dotenv()

working_dir = os.path.dirname(os.path.abspath(__file__))

class Document:
    def __init__(self, content, metadata=None):
        self.page_content = content
        self.metadata = metadata if metadata is not None else {}

def load_document(file_path):
    documents = []
    with pdfplumber.open(file_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:  # Only add non-empty pages
                # Create Document instance with page number as metadata
                documents.append(Document(content=text, metadata={"page": page_number + 1}))
    return documents

def setup_vectorstore(documents):
    embeddings = HuggingFaceEmbeddings()
    text_splitter = CharacterTextSplitter(
        separator="\n",  # Fixed typo from 'seperator' to 'separator'
        chunk_size=1000,
        chunk_overlap=200
    )

    doc_chunks = text_splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(doc_chunks, embeddings)
    return vectorstore

def create_chain(vectorstore):
    llm = ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0
    )
    retriever = vectorstore.as_retriever()
    memory = ConversationBufferMemory(
        llm=llm,
        output_key="answer",
        memory_key="chat_history",
        return_messages=True
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        chain_type="map_reduce",
        memory=memory,
        verbose=True
    )
    return chain

st.set_page_config(
    page_title="Chat with PDF",
    page_icon=" 📑",
    layout="centered"
)

st.title("Chat with your PDF  📑")

# Initialize the chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_file = st.file_uploader(
    label="Upload your PDF file.",
    type=["pdf"]
)

if uploaded_file:
    file_path = f"{working_dir}/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = setup_vectorstore(load_document(file_path))

    if "conversation_chain" not in st.session_state:
        st.session_state.conversation_chain = create_chain(st.session_state.vectorstore)

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me something...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = st.session_state.conversation_chain({"question": user_input})
        assistant_response = response["answer"]
        st.markdown(assistant_response)
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
