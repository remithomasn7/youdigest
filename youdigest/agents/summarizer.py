import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

class Summarizer:
    def __init__(self, api_key: str = None, model: str = "mistral-large-latest", temperature: float = 0):
        # Load environment variables from .env file
        load_dotenv()
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY")
        if not self.api_key:
            raise ValueError("MISTRAL_API_KEY is not set.")

        # Initialize the Mistral AI model
        self.llm = ChatMistralAI(
            model=model,
            temperature=temperature,
            mistral_api_key=self.api_key
        )
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an assistant that summarizes long transcripts into concise bullet points."),
            ("human", "{input}"),
        ])
        self.chain = self.prompt | self.llm

    def summarize(self, text: str) -> str:
        result = self.chain.invoke({"input": text})
        return result.content
