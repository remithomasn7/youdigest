from dotenv import load_dotenv
import os
from mistralai.client import MistralClient

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

client = MistralClient(api_key=MISTRAL_API_KEY)

def summarize(text):
    response = client.chat(
        model="mistral-small",  # ou "mistral-medium" selon ton plan
        messages=[{"role": "user", "content": f"Summarize this:\n{text}"}]
    )
    return response.choices[0].message.content
