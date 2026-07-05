from abc import ABC, abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    def generate(self, messages: list):
        """Generate a response from the model."""
        pass