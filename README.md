# 📑 PDF Chatbot

This project is a conversational PDF chatbot that enables users to query content from PDF files interactively. It uses **LLaMA 3.1** as the language model, **FAISS** for document retrieval and **Streamlit** for the user interface.

## Features

- **Conversational PDF Querying**: Upload a PDF file, ask questions and get relevant answers from the document.
- **LLaMA 3.1 Model**: Uses the advanced **LLaMA 3.1** model to handle natural language processing tasks.
- **RAG (Retrieval-Augmented Generation)**: Implements retrieval-augmented generation to provide precise, context-aware responses by retrieving relevant sections of the document.
- **FAISS**: Fast and efficient vector-based search to retrieve document chunks for querying.
- **Streamlit UI**: Simple, user-friendly interface to interact with the chatbot and upload PDF files.

## How It Works

1. **PDF Upload**: The user uploads a PDF, which is processed using **LangChain** to break the document into smaller chunks.
2. **Document Processing**: The document is split into chunks using a character-based splitter and converted into embeddings using **Hugging Face Embeddings**.
3. **Vector Search with FAISS**: These embeddings are stored in a **FAISS** index, allowing fast retrieval of relevant chunks when the user asks a question.
4. **Conversational Retrieval**: The system uses **LLaMA 3.1** for response generation, retrieving relevant chunks from the FAISS index and answering based on both user input and document content.
   
## Technologies Used

- **LLaMA 3.1**: A highly capable natural language processing model for conversational AI tasks.
- **FAISS**: An efficient similarity search library used for vector-based retrieval of document chunks.
- **LangChain**: Used to manage the pipeline for document chunking, embedding generation and conversational retrieval.
- **Hugging Face Embeddings**: For converting document chunks into vector embeddings.
- **Streamlit**: Framework used to build an intuitive web interface for PDF file uploads and querying.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/REPO-NAME.git

2. **Install dependencies:** Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt

3. **Run the application:** Start the Streamlit app:
   ```bash
   streamlit run app.py
   
4. **Upload PDF:** Once the app is running, upload a PDF, and start interacting with the chatbot by asking questions.
  
