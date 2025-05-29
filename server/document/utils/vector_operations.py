from langchain_core.documents import Document
from chromadb import Client
from .vector_store import get_vector_store
from uuid import uuid4

def add_documents(collection_name:str, texts: list, metadata: dict):
    ids = [str(uuid4()) for _ in range(len(texts))]
    docs = [Document(page_content=text, metadata=metadata) for text in texts]
    get_vector_store(collection_name).add_documents(documents=docs, ids=ids)
    return ids

def remove_documents(uuids: list=[]):
    return get_vector_store(collection_name).delete(ids=uuids)

def get_similar_docs(collection_name: str, query: str, k: int, filter: dict={}):
    results = get_vector_store(collection_name).similarity_search(
        query,
        k=k,
        filter=filter
    )
    return results

def delete_collection(collection_name: str):
    vector_store = get_vector_store(collection_name)
    client: Client = vector_store._client
    client.delete_collection(name=collection_name)