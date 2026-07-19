from data_layer.repositories.VectorRepository import VectorRepository
from data_layer.repositories.transaction_repository import TransactionRepository
from services.EmbeddingService import EmbeddingService
from services.VectorIndexService import VectorIndexService


class TransactionService:

    def __init__(self):
        self.transaction_repo = TransactionRepository()
        self.embedding_service = EmbeddingService()
        self.vector_repository = VectorRepository()
        self.vector_index_service = VectorIndexService(
            embedding_service=self.embedding_service,
            vector_repository=self.vector_repository,
        )

    async def save_transaction(self, transaction):

        print(f"Saving transaction to database... {transaction}")
        transaction_id = self.transaction_repo.create(transaction)
        await self.vector_index_service.add_transaction(transaction)
        return transaction_id
