from chat.ai.state import ChatRAGState
from llm.langchain_ollama_client import  get_llm_ollama_instance

def rag_search_decision_maker_node(state: ChatRAGState):
    
    model = get_llm_ollama_instance("rag_search_decision_maker", 0)
    
    
    return {
        
    }