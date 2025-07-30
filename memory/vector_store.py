#vector db

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
import os

PERSIST_DIR = "./chroma_db"

def create_vector_store(text: str):
    """Split text, embed it, and store in Chroma vector DB."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.create_documents([text])
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(docs, embedding=embeddings, persist_directory=PERSIST_DIR)
    vectordb.persist()
    return vectordb

def get_relevant_chunks(vector_store, query: str, k=4):
    """Search the vector DB and return top-k relevant documents."""
    results = vector_store.similarity_search(query, k=k)
    context = "\n".join([doc.page_content for doc in results])
    return context
