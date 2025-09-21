from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from config.settings import OPENAI_API_KEY

def get_embeddings():
    """Initialize embeddings with OpenAI."""
    return OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

def build_vectorstore(texts, embeddings):
    """Build a Chroma vectorstore from texts."""
    return Chroma.from_texts(texts, embeddings)
