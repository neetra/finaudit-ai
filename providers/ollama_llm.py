from ollama import chat
from providers.base import BaseLLM
from dotenv import load_dotenv
import os

class OllamaLLM(BaseLLM):

    def __init__(self):
        load_dotenv()
        self.model = (os.getenv("OLLAMA_MODEL") or "llama3.2").strip()

        if not self.model:
            self.model = "llama3.2"

    def generate(self, messages, role = "user"):

       

        messages = [
    {
          "role": role,
          "content": messages
    }
]
        response = chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]