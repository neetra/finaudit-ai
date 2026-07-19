
from data_layer.models.transaction import Transaction


class EmbeddingGenerator:
    @staticmethod
    def build_transaction_text(transaction: Transaction) -> str:
        return f"""
        Merchant: {transaction.merchant or 'Unknown'}
        Category: {transaction.category or 'Uncategorized'}
        Amount: {transaction.amount} {transaction.currency}
        Date: {transaction.date}
        Description: {transaction.description or ''}
        Type: {transaction.type}
        """.strip()