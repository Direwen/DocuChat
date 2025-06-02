from chat.ai.state import ChatRAGState
from llm.langchain_ollama_client import get_ollama_embedding_instance
from document.utils.vector_operations import get_similar_docs

def vector_query_node(state: ChatRAGState):
    
    model = get_ollama_embedding_instance()
    
    vector_for_user_msg = model.embed_query(state.cleaned_message)
    
    fetched_vectors = get_similar_docs(
        state.document_id,
        vector_for_user_msg,
        5
    )
    
    contents_of_fetched_vectors = [doc.page_content for doc in fetched_vectors]
        
    state.previous_qna.append({
        "question": state.cleaned_message,
        "answers": contents_of_fetched_vectors
    }) 
        
    return {
        "vector_query_results": contents_of_fetched_vectors
    }