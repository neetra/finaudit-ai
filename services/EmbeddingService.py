import os

from openai import AsyncOpenAI



class EmbeddingService:
    """
    Responsible only for generating embeddings.
    """

    def __init__(self):

        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        self.model = "text-embedding-3-small"

    async def generate_embedding(self, text: str) -> list[float]:

        response = await self.client.embeddings.create(
            model=self.model,
            input=text
        )

        return response.data[0].embedding

    async def generate_embeddings(
        self,
        texts: list[str]
    ) -> list[list[float]]:

        response = await self.client.embeddings.create(
            model=self.model,
            input=texts
        )

        return [
            item.embedding
            for item in response.data
        ]