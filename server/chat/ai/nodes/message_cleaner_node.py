from chat.ai.state import ChatRAGState
from llm.langchain_ollama_client import  get_llm_ollama_instance
from chat.ai.prompt_templates.message_cleaner_prompt_template import prompt_template

def message_cleaner_node(state: ChatRAGState):
    
    model = get_llm_ollama_instance("cleaner", 0.3)
    
    #Determine the requirement of clarification from user
    response = model.invoke(prompt_template.format(
        user_message=state.user_message
    ))
    #If required, redirect to the request user node
    
    return {
        "cleaned_message": response
    }