# 🧠 AI Research Assistant

An AI-powered assistant that extracts, summarizes, stores, and answers questions about content from web articles and academic PDFs using large language models, vector databases, and semantic search.

> Developed by Abdulrahman Sadiq

---

## 🔍 Overview

This system combines retrieval-augmented generation (RAG) with semantic embeddings to enable document understanding and conversational querying. It ingests long-form content (PDF or HTML), summarizes it using OpenAI's GPT-4 model, converts the content into vector representations, and stores them locally using ChromaDB for efficient similarity search during question-answering.

---

## 🧠 Key Capabilities

- Ingests content from:
  - Public web articles (via `requests` and HTML parsing)
  - Local or remote PDFs (via PyMuPDF)
- Summarizes content using GPT-4 via OpenAI API
- Embeds text using OpenAIEmbeddings (tiktoken-aware)
- Stores semantic vectors using ChromaDB
- Supports context-aware question answering via similarity search + LLM completion
  

---

## 🚀 Features
🌐 Web Scraping - Extract clean text from articles using BeautifulSoup.

📄 PDF Parsing - Read text from PDFs with PyMuPDF (fitz).

🧠 AI Summarization - Generate concise summaries using OpenAI GPT-4.

❓ Q&A System - Ask questions and get precise answers with semantic search (vector DB + GPT-4).

📊 Vector Database - Store and retrieve text chunks efficiently using ChromaDB and OpenAI Embeddings.

📝 Report Generation - Export summaries and Q&A sessions to Word documents.

---

## ⚙️ Architecture

       +--------------------+
       |    Web / PDF URL   |
       +--------------------+
                 |
       +--------------------+
       |  Content Extractor |
       | (scraper/pdf_loader) |
       +--------------------+
                 |
       v
    Raw Text
                 |
       +--------------------+
       |   Text Summarizer  |
       |   (GPT-4 via OpenAI) |
       +--------------------+
                 |
   Summary & Full Text
                 |
       +--------------------------+
       |   Recursive Text Splitter |
       +--------------------------+
                 |
       +----------------------+
       | OpenAIEmbeddings (API) |
       +----------------------+
                 |
     Vectors + Metadata
                 |
       +----------------------+
       |  Chroma Vector Store |
       +----------------------+
                 |
       <--- Question/Answer --->
       via Similarity Search + GPT-4

---

## 📦 Tech Stack

| Component | Tool |
|----------|------|
| LLMs      | OpenAI GPT-4 via `openai` SDK v1 |
| Vector DB | ChromaDB (`langchain_community.vectorstores.Chroma`) |
| Embeddings | `OpenAIEmbeddings` via `langchain-openai` |
| PDF Parsing | `PyMuPDF (fitz)` |
| HTML Parsing | `requests` + BeautifulSoup |
| Tokenizer | `tiktoken` |
| Env Vars | `python-dotenv` |
| Agent Framework | LangChain |

---




---
## ⚙️ How it works

📂 1. Data Ingestion
The system supports two input types:

Web URLs → Extracts text using requests + BeautifulSoup.

Local PDFs → Parses text with PyMuPDF.

✂️ 2. Text Processing
Chunks large documents into smaller segments (RecursiveCharacterTextSplitter).

Converts text into vector embeddings (OpenAIEmbeddings) for semantic search.

🧠 3. AI-Powered Analysis
Summarization → GPT-4 condenses long texts into key points.

Question Answering → Relevant chunks retrieved via ChromaDB vector search, then fed to GPT-4 for answers.

💾 4. Knowledge Retention
Stores text embeddings in a ChromaDB vector store for fast retrieval.

📤 5. Output Generation
Generates a structured Word document (output.docx) containing:

Summary of the input text.

Q&A log of all user questions and AI responses.

---

📌 Notes
GPT-4 may introduce latency. You can switch to gpt-3.5-turbo for faster responses.

ChromaDB stores vector data on disk under persist_directory. Clean up if needed.

This assistant works best on well-structured academic or article content.

🧱 Future Improvements
Add streaming support for GPT responses

Integrate HuggingFace embeddings for local fallback

Add summarization chunking for very long PDFs

Frontend Streamlit or web UI

Support multi-document memory with source ranking

📝 License
MIT License. Use, modify, or extend freely with attribution.

🙋‍♂️ Support
If you have questions or issues, open an Issue or reach out.


