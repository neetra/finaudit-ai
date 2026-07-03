# agent.py

import json
from llms.factory import LLMFactory
from agent.ChatSession import ChatSession

class Agent:

    """
    Core orchestrator of the AI system.

    Responsibilities:
    - Manage conversation flow
    - Call LLM
    - Maintain memory via ChatSession
    """
    def __init__(self, model_provider: str):
        if  model_provider is None:
            model_provider = "ollama"
        print(F"Using model provider: {model_provider}")    
        self.llm = LLMFactory.create(model_provider)
        print(f"Using llm: {type(self.llm).__name__}")
        self.chat = ChatSession()

    def run(self, user_input: str):

        self.chat.add_user_message(user_input)

        response = self.llm.generate(self.chat.history())       
       
        self.chat.add_assistant_message(
            f"Tool result: {response}"
        )        

        return response

    def reset(self):
        self.chat.clear()