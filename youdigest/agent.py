import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Initialize the Mistral AI model
llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an assistant that summarizes long transcripts into concise bullet points.",
        ),
        ("human", "{input}"),
    ]
)

# Create a chain that combines the prompt and the LLM
chain = prompt | llm

# Function to summarize text using the defined chain
def summarize(text):
    """
    Summarizes the input text using Mistral via LangChain.
    """
    result = chain.invoke({"input": text})
    return result.content
