from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {
        "messages": "How does photosynthesis work?\nIt is the process plants use to convert sunlight into energy.",
        "summary": "The conversation discussed how photosynthesis works, with an explanation that it's the process plants use to convert sunlight into energy."
    },
    {
        "messages": "I’m confused about the gamification part.\nGamification means using game-like elements to increase engagement.\nOh, I see. Thanks!",
        "summary": "The conversation clarified the meaning of gamification, explaining it's the use of game-like elements to boost engagement."
    }
]

# Define how each example should be formatted
example_prompt = PromptTemplate.from_template(
    "Messages:\n{messages}\nSummary: {summary}"
)

system_prompt = '''You are a summarization node in a RAG chatbot pipeline.
Your job is to provide a concise summary of the conversation based on the provided messages.
These messages are in chronological order but without speaker names.
Summarize the main points clearly in 2-4 sentences.

Examples:
'''

# Full prompt template with instruction and examples
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=system_prompt,
    suffix="Messages:\n{conversation_history}\nSummary:",
    input_variables=["conversation_history"]
)
