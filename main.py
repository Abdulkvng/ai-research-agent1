
# ai - research - agent

import os  # Used to check if file paths exist

# Import your helper modules
from retriever.web_scraper import scrape_article          # Scrapes web articles
from retriever.document_loader import load_pdf_text       # Loads text from PDF files
from llm_agent.summarizer import summarize                # Summarizes text using LLM
from llm_agent.qa_agent import ask_question               # Q&A using retrieved context and LLM
from memory.vector_store import create_vector_store, get_relevant_chunks  # Vector DB setup and search
from outputs.report_generator import generate_doc         # Creates a Word document output

def main():
    print("\n🔍 AI Research Assistant\n")

    # Prompt the user to choose the input type: web or PDF
    source_type = input("Choose input type (web/pdf): ").strip().lower()

    # Retrieve and process input based on the user's choice
    if source_type == "web":
        url = input("Enter the URL: ")
        text = scrape_article(url)  # Scrape article content from the web
    elif source_type == "pdf":
        pdf_path = input("Enter path to PDF file: ")
        if not os.path.exists(pdf_path):  # Validate that the file exists
            print("❌ File not found.")
            return
        text = load_pdf_text(pdf_path)  # Load and extract text from the PDF
    else:
        print("❌ Invalid input type.")
        return

    # Step 1: Summarize the content using an LLM
    print("\n📖 Summarizing content...")
    summary = summarize(text)
    print("\n✅ Summary:\n", summary)

    # Step 2: Create a vector store so we can do similarity search on document chunks
    print("\n💾 Creating memory store...")
    vector_store = create_vector_store(text)

    # Step 3: Let the user ask questions based on the document
    questions = []
    q_and_a = {}

    while True:
        q = input("\nAsk a question about the document (or type 'done'): ")
        if q.lower() == 'done':  # Exit loop when user types 'done'
            break
        # Retrieve the most relevant chunks to the question
        relevant_chunks = get_relevant_chunks(vector_store, q)
        # Use LLM to answer the question using the retrieved context
        answer = ask_question(relevant_chunks, q)
        # Store the Q&A for the final report
        q_and_a[q] = answer
        print("🧠", answer)

    # Step 4: Generate a .docx report with the summary and Q&A section
    print("\n📝 Generating output report...")
    generate_doc(summary, q_and_a)
    print("✅ Report saved as output.docx")

# Run the script if executed directly (not imported)
if __name__ == "__main__":
    main()
