from ollama import chat
from llms.base import BaseLLM
from dotenv import load_dotenv
import os

class OllamaLLM(BaseLLM):

    def __init__(self):
        load_dotenv()
        self.model = os.getenv("OLLAMA_MODEL")

    def generate(self, messages):

        response = chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]