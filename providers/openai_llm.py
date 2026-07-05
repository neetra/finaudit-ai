# openai_llm.py

import os
from openai import OpenAI
from dotenv import load_dotenv
class OpenAILLM:

    def __init__(self, model="gpt-5"):
        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.model = (os.getenv("OPENAI_MODEL") or os.getenv("OPENAI_MODEL_NAME") or model or "gpt-4o-mini").strip()

        if not self.model:
            self.model = "gpt-4o-mini"

    def generate(self, messages):

        response = self.client.responses.create(
            model=self.model,
            input=messages,
        )

        return response.output_text