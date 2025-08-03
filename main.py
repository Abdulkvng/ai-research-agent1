# ai-research-agent/main.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Imports
from retriever.document_loader import load_document
from llm_agent.summarizer import summarize
from llm_agent.qa_agent import ask_question
from memory.vector_store import create_vector_store, get_relevant_chunks
from outputs.report_generator import generate_doc


def main():
    print("\n🔍 AI Research Assistant\n")

    source_type = input("Choose input type (web/pdf): ").strip().lower()
    path_or_url = input("Enter path or URL: ").strip()

    # Load content
    text = load_document(source_type, path_or_url)

    if not text.strip():
        print("❌ No text was extracted from the input. Exiting.")
        return

    # Summarize
    print("\n📖 Summarizing content...")
    summary = summarize(text)
    print("\n✅ Summary:\n", summary)

    # Vector Store
    print("\n💾 Creating memory store...")
    vector_store = create_vector_store(text)

    # Q&A Loop
    q_and_a = {}
    while True:
        q = input("\nAsk a question about the document (or type 'done'): ").strip()
        if q.lower() == "done":
            break
        chunks = get_relevant_chunks(vector_store, q)
        answer = ask_question(chunks, q)
        q_and_a[q] = answer
        print("🧠", answer)

    # Generate Output Report
    print("\n📝 Generating output report...")
    generate_doc(summary, q_and_a)
    print("✅ Report saved as output.docx")


if __name__ == "__main__":
    main()
