import os
from urllib import response
from xmlrpc import client
from dotenv import load_dotenv
from openai import OpenAI
from providers.base import BaseLLM



class AzureOpenAILLM(BaseLLM):

    def __init__(self):
        load_dotenv()
        self.client = OpenAI(
            base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_APIKEY")
        )
        self.model = (os.getenv("AZURE_OPENAI_MODEL") or os.getenv("AZURE_OPENAI_DEPLOYMENT") or "gpt-4o-mini").strip()

        if not self.model:
            self.model = "gpt-4o-mini"

    def generate(self, messages):        

        response = self.client.responses.create(
        model=self.model,
        input=messages,
    )
        return response.output[0].content[0].text

