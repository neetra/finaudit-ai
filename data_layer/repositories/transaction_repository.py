from data_layer.models.transaction import Transaction
from data_layer.repositories.base import BaseRepository


class TransactionRepository(BaseRepository):
    def create(self, tx: Transaction) -> int:
        row = self.execute_one(
            """
            INSERT INTO transactions (user_id, date, type, amount, currency, description, category)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (tx.user_id, tx.date, tx.type, tx.amount, tx.currency, tx.description, tx.category),
        )
        return row[0]

    def get_by_id(self, transaction_id: int) -> Transaction | None:
        row = self.execute_one(
            """
            SELECT id, user_id, date, type, amount, currency, description, category, created_at
            FROM transactions
            WHERE id = %s
            """,
            (transaction_id,),
        )
        return Transaction(*row) if row else None

    def list_for_user(self, user_id: int, limit: int = 100) -> list[Transaction]:
        rows = self.execute_many(
            """
            SELECT id, user_id, date, type, amount, currency, description, category, created_at
            FROM transactions
            WHERE user_id = %s
            ORDER BY date DESC
            LIMIT %s
            """,
            (user_id, limit),
        )
        return [Transaction(*row) for row in rows]

    def delete(self, transaction_id: int) -> None:
        self.execute("DELETE FROM transactions WHERE id = %s", (transaction_id,))
