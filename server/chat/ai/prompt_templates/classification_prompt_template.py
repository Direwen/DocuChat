from langchain.prompts import PromptTemplate, FewShotPromptTemplate

# Define examples with only True/False classification
examples = [
    {"query": "Tell me about AI.", "classification": "False"},
    {"query": "fjsdkjflsdklsdkflsd", "classification": "True"},
    {"query": "How does", "classification": "True"},
    {"query": "What's this document about", "classification": "False"}
]

# Define how each example should be formatted
example_prompt = PromptTemplate.from_template(
    "User Query: {query}\nClassification: {classification}"
)

# Define system prompt / prefix
system_prompt = '''You are a classifier for user messages in a RAG chatbot pipeline.
Your task is to determine whether a user message is clear enough to proceed with retrieval and generation, or if it needs further clarification due to being incomplete, ambiguous, or nonsensical.

Respond ONLY with "True" (needs clarification) or "False" (clear enough).

Examples:
'''

# Create FewShotPromptTemplate
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=system_prompt,
    suffix="User Query: {user_message}\nClassification:",
    input_variables=["user_message"]
)