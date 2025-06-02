from chat.ai.state import ChatRAGState
from llm.langchain_ollama_client import  get_llm_ollama_instance
from chat.ai.prompt_templates.responder_prompt_template import prompt_template

def responder_node(state: ChatRAGState):
    
    model = get_llm_ollama_instance("responder", 0.4)
    
    response = moodel.invoke(prompt_template.format(
        context="\n".join(state.vector_query_results),
        conversation_summary=state.conversation_summary,
        user_question=state.user_message
    ))
    
    return {
        "final_response": response
    }