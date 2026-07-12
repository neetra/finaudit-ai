from data_layer.models import FinancialQuery
from data_layer.models.RetrievalResult import RetrievalResult
from data_layer.repositories.transaction_repository import TransactionRepository


class TransactionRetriever:
    """
    Retrieves relevant transactions for RAG.

    Phase 1:
        - Fetch recent transactions.
        - No NLP or semantic search yet.

    Phase 2:
        - Parse dates
        - Parse merchants
        - Parse categories

    Phase 3:
        - Hybrid SQL + Vector Search
    """

    def __init__(self):
        self._repository = TransactionRepository()

    def retrieve(
        self,
        financialQuery : FinancialQuery
    ) -> RetrievalResult:
        """
        Retrieve transactions relevant to the user's question.
        """

        # For now, retrieve the latest 50 transactions.
       
        transactions =  self._repository.list_for_user(
            user_id=financialQuery.user_id,
            limit=50,
        )


        return RetrievalResult(
            question=financialQuery.question,
            transactions=transactions,
        )