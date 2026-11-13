# FastAPI RAG Document Q&A

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions based on their content.

Built using **Python, FastAPI, OpenAI Embeddings, ChromaDB, and the OpenAI Responses API**.

## 🚀 Project Overview

This project implements a simple RAG pipeline that retrieves relevant information from uploaded PDF documents and uses an LLM to generate context-aware answers.

Instead of sending the entire document to the LLM for every question, the application retrieves only the most relevant text chunks from ChromaDB and provides them as context to the model.

## ✨ Features

- Upload PDF documents through a REST API.
- Extract text from PDF files using PyPDF.
- Split extracted text into smaller chunks.
- Generate text embeddings using OpenAI Embeddings API.
- Store document chunks and embeddings in ChromaDB.
- Convert user questions into embeddings.
- Retrieve relevant document chunks using vector similarity search.
- Generate answers using the OpenAI Responses API.
- Return source page and chunk information with answers.
- Support multiple uploaded documents using document IDs.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API development |
| Uvicorn | ASGI server |
| PyPDF | PDF text extraction |
| OpenAI Embeddings | Text-to-vector conversion |
| ChromaDB | Vector database |
| OpenAI Responses API | LLM response generation |
| Pydantic | Request validation |
| python-dotenv | Environment variable management |

## 🏗️ Architecture

The application consists of two main workflows.

### 1. Document Ingestion Pipeline

```text
PDF Upload
    |
    v
PDF Text Extraction
    |
    v
Text Chunking
    |
    v
Generate Embeddings
    |
    v
Store in ChromaDB
    |
    v
Return Document ID
```

### 2. Question Answering Pipeline

```text
User Question
    |
    v
Generate Query Embedding
    |
    v
Search ChromaDB
    |
    v
Retrieve Relevant Chunks
    |
    v
Build Prompt
    |
    v
OpenAI Responses API
    |
    v
Generate Answer
    |
    v
Return Answer + Sources
```

## 📁 Project Structure

```text
fastapi-rag-document-qa/
│
├── data/
│   ├── uploads/
│   └── chroma_db/
│
├── src/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── chat_routes.py
│   │   │   └── document_routes.py
│   │   │
│   │   └── schemas/
│   │       └── chat_schema.py
│   │
│   ├── preprocessing/
│   │   ├── pdf_reader.py
│   │   └── text_chunker.py
│   │
│   ├── services/
│   │   ├── document_service.py
│   │   ├── embedding_service.py
│   │   ├── generation_service.py
│   │   ├── retrieval_service.py
│   │   └── vector_service.py
│   │
│   ├── config.py
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-rag-document-qa.git

cd fastapi-rag-document-qa
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

The application uses the OpenAI API for embeddings and text generation.

**Note:** OpenAI API usage is billed separately. The Python libraries and local ChromaDB storage are free to use, but OpenAI API calls are not generally free.

### 5. Run the application

```bash
uvicorn src.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## 📡 API Endpoints

### 1. Health Check

**GET** `/health`

Checks whether the application is running.

Example response:

```json
{
  "status": "healthy",
  "message": "RAG API is running"
}
```

### 2. Upload Document

**POST** `/documents/upload`

Uploads a PDF document, extracts its text, creates chunks, generates embeddings, and stores them in ChromaDB.

Request:

```text
Content-Type: multipart/form-data

file: python_notes.pdf
```

Example response:

```json
{
  "message": "Document uploaded successfully",
  "document_id": "a123-456",
  "filename": "python.pdf",
  "total_pages": 10,
  "total_chunks": 25
}
```

### 3. Ask a Question

**POST** `/chat/query`

Accepts a document ID and user question.

Request body:

```json
{
  "document_id": "a123-456",
  "question": "What is Python?"
}
```

Example response:

```json
{
  "question": "What is Python?",
  "answer": "Python is a high-level programming language...",
  "sources": [
    {
      "page": 1,
      "chunk": 1
    },
    {
      "page": 2,
      "chunk": 1
    }
  ]
}
```

*Example responses are illustrative.*

## 🧪 Testing the API

FastAPI provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test the complete workflow:

1. Upload a PDF using `/documents/upload`.
2. Copy the returned `document_id`.
3. Open `/chat/query`.
4. Provide the document ID and your question.
5. Execute the request.
6. Receive an answer with source references.

## 🧠 Core RAG Concepts Implemented

| Concept | Implementation |
|---|---|
| Document ingestion | PDF upload and extraction |
| Chunking | Splitting documents into smaller text segments |
| Embeddings | Converting text into numerical vectors |
| Vector database | Storing and searching vectors |
| Semantic search | Retrieving relevant chunks |
| Prompt engineering | Combining instructions, context and question |
| LLM generation | Generating context-aware answers |
| Metadata filtering | Searching chunks by document ID |

## 📚 Learning Objective

This project was developed to understand the complete RAG workflow, from document ingestion and embedding generation to semantic retrieval and LLM-based answer generation.

It demonstrates how traditional backend development with FastAPI can be integrated with modern Generative AI technologies.

---

**Built with Python, FastAPI, ChromaDB and Generative AI.**