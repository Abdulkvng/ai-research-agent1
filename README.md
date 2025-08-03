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
| HTML Parsing | `requests` + BeautifulSoup (if implemented) |
| Tokenizer | `tiktoken` |
| Env Vars | `python-dotenv` |
| Agent Framework | LangChain |

---

## 📁 Project Structure

ai-research-agent/
├── main.py # CLI entry point
├── .env.example # Sample environment file
├── requirements.txt # Dependency list
├── README.md # Project documentation
│
├── retriever/
│ └── pdf_loader.py # Handles both URL and local PDF parsing
│
├── llm_agent/
│ ├── summarizer.py # Summarizes input text using OpenAI
│ └── qa_agent.py # Performs semantic Q&A with GPT-4
│
├── memory/
│ └── vector_store.py # Vector DB management using Chroma
│
├── outputs/ # Optional: logs or saved summaries
└── venv/ # Local virtual environment (excluded from Git)


---

## 🔐 Environment Setup

### 1. Clone & Setup

```bash
git clone https://github.com/YOUR_USERNAME/ai-research-agent.git
cd ai-research-agent
python3 -m venv venv
source venv/bin/activate

2. Install Dependencies
```bash
pip install -r requirements.txt
3. Set Environment Variables
bash
cp .env.example .env

🔍 AI Research Assistant

Choose input type (web/pdf): pdf
Enter PDF path or URL: https://arxiv.org/pdf/2402.01234.pdf

📖 Summarizing content...
✅ Summary: [short GPT-4 summary]

Ask a question (or type 'exit'): What is the main contribution?
🤖 Answer: The authors propose a novel approach to...



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

yaml
Copy
Edit

---

## ✅ Next Step

- Replace `YOUR_USERNAME` with your GitHub username
- Save this as `README.md` in your project root
- You're ready to `git add . && git commit -m "Initial commit"` and push!

Would you like the `.gitignore` or pre-filled `pdf_loader.py` as well?
