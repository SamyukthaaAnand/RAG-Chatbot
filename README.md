📑 PDF Chatbot

This project is a PDF Chatbot built using Streamlit, which allows users to upload PDF files and interact with the content through a conversational interface. Powered by LangChain, FAISS, HuggingFace Embeddings, and the LLaMA 3.1 language model, the chatbot retrieves relevant content from PDFs and provides accurate, context-aware answers to user queries.

Features

PDF Upload & Query: Users can upload PDF files and ask questions about the content, receiving detailed and relevant answers.
Document Chunking: The chatbot splits the document into manageable chunks to efficiently process large PDFs.
Vector Embeddings & Similarity Search: Using HuggingFace Embeddings and FAISS, the chatbot converts text into vector embeddings and performs fast similarity searches.
Retrieval-Augmented Generation (RAG): Combines document retrieval with language generation to improve response accuracy.
Advanced Language Model: Powered by LLaMA 3.1 via ChatGroq, the chatbot provides context-aware and natural language responses.
Persistent Chat History: The conversational memory stores previous interactions, allowing seamless and continuous querying.
Technologies Used

Streamlit: Frontend framework to build the interactive web app for file upload and user queries.
LangChain: Framework for document chunking, retrieval, and integration with large language models (LLMs).
HuggingFace Embeddings: Converts document text into vector embeddings for similarity search.
FAISS: Used for efficient similarity search to find relevant content in large documents.
RAG (Retrieval-Augmented Generation): Enhances accuracy by retrieving relevant information before generating responses.
LLaMA 3.1 via ChatGroq: Language model responsible for providing intelligent, context-aware responses to user queries.
Installation

To get started, clone the repository and install the required dependencies.

Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/pdf-chatbot.git
cd pdf-chatbot
Install the dependencies:
bash
Copy code
pip install -r requirements.txt
Ensure that requirements.txt includes the following dependencies:

txt
Copy code
streamlit
pdfplumber
langchain
huggingface-hub
faiss-cpu
ChatGroq
python-dotenv
openai
llama-cpp-python
Set up environment variables:
Create a .env file in the root directory with the following variables:

env
Copy code
OPENAI_API_KEY=your_openai_api_key
Run the Streamlit app:
bash
Copy code
streamlit run app.py
Usage

Upload PDF: After launching the app, upload a PDF file by clicking the upload button.
Ask Questions: Once the PDF is uploaded, type your questions in the chat input field.
View Responses: The chatbot will return answers based on the content of the uploaded PDF. Chat history is maintained for ongoing interaction.
Project Workflow

PDF Upload: Users upload a PDF file via the Streamlit interface.
Document Processing: The PDF is processed using pdfplumber to extract text.
Text Chunking: The text is split into smaller, manageable chunks using LangChain’s text splitter.
Embedding Creation: The document chunks are converted into vector embeddings using HuggingFace Embeddings.
Similarity Search: FAISS performs fast similarity searches on the embeddings to retrieve the most relevant content.
Question Answering: Queries are answered using LLaMA 3.1 via ChatGroq, which provides accurate and context-aware responses by leveraging the document's content.
Example

Once the app is running, a typical interaction might look like this:

User: "What is the main conclusion of the report?"
Chatbot: "The report concludes that..."
