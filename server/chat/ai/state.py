from typing import TypedDict, List

class ChatRAGState(TypedDict):

    # 🌿 Raw inputs
    user_message: str  # original user message
    user_intent: str | None = None  # e.g., "ask_new", "clarify", "follow_up"
    cleaned_message: str | None = None  # cleaned or extracted user extent
    
    # Conditional inputs
    is_rag_required: bool = False
    is_clarification_required: bool = False

    # 🌿 Conversation memory
    conversation_summary: str | None = None  # summarized past conversation
    previous_qna: list[dict[str, list[str]]] | None = None #Will store last 3 or 5 questions and answers (embedding ids)

    # 🌿 Final outputs
    final_response: str | None = None  # final LLM-generated response to user
