import os
import sys
from dotenv import load_dotenv
from django.conf import settings
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

load_dotenv()

# Initialize embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")
# Build persist directory using BASE_DIR
persist_directory = os.path.join(settings.BASE_DIR, os.environ.get("CHROMA_DB_DIRECTORY", "chroma_db"))


def get_vector_store(collection_name: str):
    return Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=persist_directory,
    )
    
def get_embedding_dimension():
    test_vector = embeddings.embed_query("test")
    return len(test_vector)