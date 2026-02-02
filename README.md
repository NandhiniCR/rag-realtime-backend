📌 Project Overview

This project is a Local Retrieval-Augmented Generation (RAG) Backend System designed to ingest PDF documents, process them into searchable knowledge chunks, and answer user queries using semantic search — without relying on paid OpenAI APIs.

The system follows a complete RAG pipeline, including document ingestion, text chunking, vector embedding, similarity-based retrieval, and response generation. All components are built using open-source tools, making the project cost-free, reproducible, and production-friendly.

This project was built step by step from scratch, addressing real-world engineering challenges such as dependency conflicts, Python version incompatibilities, LangChain breaking changes, API quota limits, and secure environment configuration. The final solution is a fully functional backend that can later be extended with a FastAPI service, UI layer, conversational memory, or local LLMs like LLaMA or Mistral.

🎯 Key Objectives

Build a real-time document question-answering system

Implement RAG architecture using open-source tools

Avoid paid APIs and quota limitations

Follow clean project structure and best practices

Deploy and version-control the project on GitHub

Make the system extensible for future upgrades

🧠 What This Project Demonstrates

Practical understanding of RAG (Retrieval-Augmented Generation)

Experience with LangChain ecosystem

Vector search using FAISS

Secure environment handling using .env

Debugging and resolving real production-level issues

GitHub-based deployment and version control

Ability to document and explain engineering decisions clearly

🏗️ High-Level Architecture

Document Ingestion
PDFs are loaded from the data/raw/ directory.

Text Chunking
Documents are split into smaller, overlapping chunks for better retrieval accuracy.

Vector Embeddings
Text chunks are converted into vector embeddings using local/open-source embedding models.

Vector Store (FAISS)
Embeddings are stored in a FAISS index for fast similarity search.

Query & Retrieval
User queries are embedded and matched against stored vectors to retrieve the most relevant chunks.

Response Generation (Extensible)
Retrieved context can be passed to a local or remote LLM for answer generation.

🚀 Current Status

✅ Core RAG backend completed
✅ PDF ingestion and chunking implemented
✅ Vector search with FAISS working
✅ GitHub repository deployed
✅ Professional documentation completed

🔮 Future Enhancements

Add FastAPI backend for API-based access

Add Streamlit UI for chat-based interaction

Implement conversational memory

Integrate local LLMs (LLaMA / Mistral)

Dockerize for production deployment
