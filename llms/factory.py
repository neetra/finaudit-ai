from llms.ollama_llm import OllamaLLM
from llms.openai_llm import OpenAILLM


PROVIDER_CLASSES = {
    "ollama": OllamaLLM,
    "openai": OpenAILLM,
}


class LLMFactory:

    @staticmethod
    def create(provider: str):
        if not provider:
            raise ValueError("MODEL_PROVIDER is required. Set MODEL_PROVIDER in .env.")

        key = provider.strip().lower()
        provider_cls = PROVIDER_CLASSES.get(key)

        if provider_cls is None:
            supported = ", ".join(sorted(PROVIDER_CLASSES))
            raise ValueError(
                f"Unknown provider: {provider}. Supported providers: {supported}"
            )

        return provider_cls()
