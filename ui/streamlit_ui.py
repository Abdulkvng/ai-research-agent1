
import streamlit as st
from retriever.web_scraper import scrape_article
from llm_agent.summarizer import summarize

st.title("AI Personal Research Assistant")

url = st.text_input("Enter article URL:")
if url:
    text = scrape_article(url)
    summary = summarize(text)
    st.subheader("Summary")
    st.write(summary)
