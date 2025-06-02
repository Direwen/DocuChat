from langchain_ollama import OllamaLLM
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

_chat_ollama_instances = {}
_llm_ollama_instances = {}
_ollama_embedding_instance = None

ollama_model = os.environ.get("OLLAMA_LLM_MODEL")
ollama_embedding_model = os.environ.get("OLLAMA_EMBEDDING_MODEL")
temperature = float(os.environ.get("OLLAMA_LLM_TEMPERATURE", 0.8))
num_predict = int(os.environ.get("OLLAMA_LLM_NUM_PREDICT", 256))

def get_chat_ollama_instance(name, temp=temperature, num_predict=num_predict):
    global _chat_ollama_instances
    
    if name not in _chat_ollama_instances:
        _chat_ollama_instances[name] = ChatOllama(
            model=ollama_model,
            temperature=temp,
            num_predict=num_predict,
        )
            
    return _chat_ollama_instances[name]

def get_llm_ollama_instance(name, temp=temperature):
    global _llm_ollama_instances
    
    if name not in _llm_ollama_instances:
        _llm_ollama_instances[name] = OllamaLLM(
            model=ollama_model,
            temperature=temp,
        )
        
    return _llm_ollama_instances[name]

def get_ollama_embedding_instance():
    if not _ollama_embedding_instance:
        _ollama_embedding_instance = OllamaEmbeddings(model=ollama_embedding_model)
    return _ollama_embedding_instance