from chat.ai.state import ChatRAGState
from llm.langchain_ollama_client import  get_llm_ollama_instance
from chat.ai.prompt_templates.chat_summarizer_prompt_template import prompt_template

def chat_summarizer_node(state: ChatRAGState):
    
    model = get_llm_ollama_instance("chat_summarizer", 0.2)
    
    response = model.invoke(prompt_template.format(
        conversation_history=state.conversation_history
    ))
    
    return {
        "conversation_summary": response
    }