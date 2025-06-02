from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("""
You are an assistant inside a RAG chatbot system.

Your task:
- Answer the user's question **only** using the provided context and past conversation summary.
- If the context or summary do **not** contain the answer or the question is unrelated, **refuse informally** (e.g., “Sorry, I don’t know about that.”).

---
Context:
{context}

Conversation Summary:
{conversation_summary}

User Question:
{user_question}

Assistant Response:
""")
