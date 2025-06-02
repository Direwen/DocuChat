from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {
        "input": "Ok, I see it now but what's exactly related to this gamification?",
        "output": "What is related to gamification?"
    },
    {
        "input": "So like, how does photosynthesis actually work? Can you explain again?",
        "output": "How does photosynthesis work?"
    }
]

# Define how each example should be formatted
example_prompt = PromptTemplate.from_template("User Message: {input}\nOutput:{output}")

system_prompt = '''You are a preprocessing node in a RAG chatbot pipeline.
Your job is to extract the core question from the user message.
Remove unnecessary words, repetitions, or filler language.

Examples:
'''

# Full prompt template with instruction and examples
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=system_prompt,
    suffix="User Message: {user_message}\nOutput:",
    input_variables=["user_message"]
)