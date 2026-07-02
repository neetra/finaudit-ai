# llm.py
#Notice something important:
"""
The rest of our project doesn't know we're using Ollama.

Tomorrow we could switch to:

OpenAI
Azure OpenAI
Anthropic
Gemini

by changing only llm.py.

This abstraction is exactly what production systems aim for.
from ollama import chat

"""
from ollama import chat
class LocalLLM:

    def __init__(self, model="llama3.2"):
        self.model = model

    def generate(self, messages):

        response = chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]