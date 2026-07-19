from data_layer.embeddings.EmbeddingGenerator import EmbeddingGenerator


class VectorIndexService:
    def __init__(self, embedding_service, vector_repository):
        self.embedding_service = embedding_service
        self.vector_repository = vector_repository

    async def add_transaction(self, transaction):

        content = EmbeddingGenerator.build_transaction_text(transaction)

        embedding = await self.embedding_service.generate_embedding(content)

        self.vector_repository.insert_embedding(
            transaction.id,
            transaction.user_id,
            content,
            embedding,
        )
