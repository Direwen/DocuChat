from chat.ai.state import ChatRAGState
from llm.langchain_ollama_client import  get_llm_ollama_instance, get_chat_ollama_instance

def chat_summarizer_node(state: ChatRAGState):
    
    model = get_llm_ollama_instance("chat_summarizer", 0.2)
    
    return {
        
    }