from abc import ABC, abstractmethod

class BaseTool(ABC):

    def __init__(self, name: str):
        self.name = name
        print(f"-> Initializing Tool: {self.name}")

    @abstractmethod
    async def execute(self, **kwargs):
        pass