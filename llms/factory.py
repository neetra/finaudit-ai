from llms.ollama_llm import OllamaLLM
from llms.openai_llm import OpenAILLM


class LLMFactory:

    @staticmethod
    def create(provider: str):

        if provider.lower() == "ollama":
            return OllamaLLM()

        if provider.lower() == "openai":
            return OpenAILLM()

        raise ValueError(f"Unknown provider: {provider}")