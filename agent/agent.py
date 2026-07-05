from abc import ABC, abstractmethod

from providers.llmfactory import LLMFactory
from agent.ChatSession import ChatSession


class BaseAgent(ABC):
    """Abstract contract for agents in the financial audit system."""

    def __init__(self, model_provider: str, agent_name: str = "agent", instructions: str = None, tools: list = None):
        if model_provider is None:
            model_provider = "ollama"
        print(f"Using model provider: {model_provider}")
        self.llm = LLMFactory.create(model_provider)
        self.name = agent_name
        self.instructions = instructions or ""
        self.tools = tools or []
        print(f"Using llm: {type(self.llm).__name__}")
        self.chat = ChatSession()
        if self.instructions:
            self.chat.add_system_message(self.instructions)

    def run(self, user_input: str):
        self.chat.add_user_message(user_input)
        response = self.llm.generate(self.chat.history())
        self.chat.add_assistant_message(f"Tool result: {response}")
        return response

    def reset(self):
        self.chat.clear()

    @abstractmethod
    def process(self, user_input: str):
        raise NotImplementedError