from chat.ai.state import ChatRAGState
from llm.langchain_ollama_client import  get_llm_ollama_instance
from chat.ai.prompt_templates.classification_prompt_template import prompt_template

def classification_node(state: ChatRAGState):
    
    model = get_llm_ollama_instance("classification", 0)
    
    #Determine the requirement of clarification from user
    response = model.invoke(prompt_template.format(
        
    ))
    #If required, redirect to the request user node
    
    return {
        "is_clarification_required": response
    }