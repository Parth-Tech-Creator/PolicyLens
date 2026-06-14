# PolicyLens — AI-Based Automated Legal Document Summarization

## Overview

PolicyLens is an AI-powered legal and government policy document analysis platform designed to simplify long and complex documents through intelligent summarization, semantic retrieval, automated risk detection, and retrieval-augmented question answering.

The system processes lengthy PDF documents using a multi-stage AI pipeline that combines Natural Language Processing (NLP), semantic embeddings, vector retrieval, large language models (LLMs), and cloud deployment technologies to generate transparent and verifiable summaries.

Unlike traditional summarization systems, PolicyLens provides:
- Source-traceable summaries
- Automated legal risk detection
- Depth-calibrated summarization
- Retrieval-Augmented Generation (RAG) chatbot
- Cloud-based multi-user accessibility
- Real-time semantic document analysis

---

# Key Features

## AI-Based Document Summarization

Generate concise summaries from lengthy legal and policy documents using LLM-based abstractive summarization.

### Supported Summary Depths
- Brief Summary
- Standard Summary
- Detailed Analysis

---

## Source Traceability

Every generated summary sentence is mapped back to the original source paragraph using semantic similarity retrieval through FAISS indexing.

This improves:
- Transparency
- Verifiability
- Trustworthiness
- Hallucination reduction

---

## Semantic Search & Retrieval

The system uses:
- `all-MiniLM-L6-v2` sentence embeddings
- FAISS vector indexing

to enable fast semantic retrieval across long documents.

---

## Automated Legal Risk Detection

PolicyLens detects risky legal clauses such as:
- Unlimited liability
- Mandatory arbitration
- Auto-renewal traps
- Data-sharing clauses
- Hidden fees
- Unilateral modifications
- Privacy-invasive clauses

The system supports 15 categories of legal risk detection.

---

## RAG Chatbot (PolicyBot)

The integrated chatbot enables users to ask questions directly about uploaded documents.

The chatbot:
- Retrieves relevant document chunks
- Uses retrieval-augmented generation (RAG)
- Produces grounded answers
- Reduces hallucination risk

---

## Cloud Deployment

Production deployment includes:
- Frontend hosted on Vercel
- Backend hosted on Render
- MongoDB Atlas database
- Google OAuth 2.0 authentication
- JWT-based session management

---

# System Architecture

```text
                ┌─────────────────────┐
                │    React Frontend   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    FastAPI Backend  │
                └──────────┬──────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼

 ┌─────────────┐   ┌────────────────┐   ┌─────────────┐
 │ OpenRouter  │   │ FAISS Vector   │   │ MongoDB     │
 │ Mistral-7B  │   │ Database       │   │ Atlas       │
 └─────────────┘   └────────────────┘   └─────────────┘
```

---

# AI Pipeline

## Stage 1 — PDF Parsing

Extracts text from uploaded PDF documents using:
- PyMuPDF
- pdfplumber

---

## Stage 2 — Text Cleaning

Performs:
- Whitespace normalization
- Noise removal
- Formatting cleanup

---

## Stage 3 — Context-Aware Segmentation

Splits long documents into semantically meaningful chunks while preserving sentence boundaries.

---

## Stage 4 — Embedding Generation & FAISS Indexing

Generates semantic embeddings using:
- `all-MiniLM-L6-v2`

Stores vectors inside:
- FAISS vector index

---

## Stage 5 — Red Flag Detection

Two-stage risk analysis:
1. Regex-based legal clause detection
2. AI-generated plain-English explanations

---

## Stage 6 — Depth-Calibrated Summarization

Uses:
- Mistral-7B-Instruct via OpenRouter API

Generates:
- Brief summaries
- Standard summaries
- Detailed summaries

---

## Stage 7 — Traceable Summary Mapping

Each summary sentence is mapped back to the most semantically similar source paragraph.

---

## Stage 8 — Key Point Extraction

Uses centroid-based semantic analysis to identify the most representative document clauses.

---

## Stage 9 — Retrieval-Augmented Chatbot

Implements:
- Semantic retrieval
- Context injection
- Grounded LLM answering

---

# Technologies Used

## Frontend
- React.js
- Vite
- Tailwind CSS

## Backend
- FastAPI
- Python 3.10+

## AI / NLP
- Sentence Transformers
- all-MiniLM-L6-v2
- FAISS
- OpenRouter API
- Mistral-7B-Instruct

## Database
- MongoDB Atlas

## Authentication
- Google OAuth 2.0
- JWT Authentication

## Deployment
- Vercel
- Render

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/yourusername/policylens.git
cd policylens
```

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Backend Server

```bash
uvicorn app:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

# Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key
MONGODB_URI=your_mongodb_uri
JWT_SECRET=your_secret_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

---

# API Endpoints

## Upload Document

```http
POST /upload
```

---

## Generate Summary

```http
POST /summarize
```

Parameters:
- `depth = brief`
- `depth = standard`
- `depth = detailed`

---

## Query Chatbot

```http
POST /query
```

---

## Risk Detection

```http
POST /risk-analysis
```

---

# Advantages of PolicyLens

- Reduces legal document analysis time
- Improves accessibility of government documents
- Enhances transparency in AI summarization
- Provides source verification
- Detects risky legal clauses automatically
- Supports interactive document exploration

---

# Current Limitations

- English-language support only
- No OCR support for scanned PDFs
- FAISS index currently stored in-memory
- Free-tier cloud deployment limitations
- OpenRouter request-rate limits

---

# Future Scope

- OCR integration
- Multilingual legal analysis
- Persistent vector databases
- Enterprise deployment
- Indian legal dataset fine-tuning
- Advanced legal reasoning models
- Real-time collaborative document analysis

---

# Research Contributions

PolicyLens contributes:
- Source-traceable legal summarization
- Hybrid semantic retrieval architecture
- Explainable AI-based legal risk detection
- Depth-controlled AI summarization
- Production-style legal AI deployment

---

# Conclusion

PolicyLens demonstrates how modern NLP, semantic retrieval, vector databases, and large language models can be integrated into a unified framework for transparent and scalable legal document analysis.

The system bridges the gap between AI summarization and trustworthy legal document interpretation by combining:
- Semantic retrieval
- Traceability
- Automated risk analysis
- Grounded conversational AI

---

# Authors

- Arbind Malava
- Parth
- Ayush Thakur
- Bhupender Singh

---

# Project Guide

Dr. Abhishilpa Nandini  
Assistant Professor  
Department of Computer Science & Engineering  
Chandigarh Engineering College Jhanjeri, Mohali

---

# License

This project is developed for academic and research purposes.
