import uuid
from data_layer.repositories.base import BaseRepository


class VectorRepository(BaseRepository):
    def insert_embedding(
        self,
        transaction_id: uuid.UUID,
        user_id: uuid.UUID,
        content: str,
        embedding: list[float],
    ):
        """
        Inserts a transaction embedding into pgvector table.
        """

        # pgvector expects vector format like: [0.1,0.2,0.3]
        embedding_str = "[" + ",".join(map(str, embedding)) + "]"

        query = """
        INSERT INTO transaction_embeddings
        (id, transaction_id, user_id, content, embedding)
        VALUES (%s, %s, %s, %s, %s::vector)
        """

        self.execute(
            query,
            (
                uuid.uuid4(),
                transaction_id,
                user_id,
                content,
                embedding_str,
            ),
        )

    def similarity_search(
        self,
        user_id: uuid.UUID,
        embedding: list[float],
        top_k: int = 5,
    ):
        """
        Returns most similar transactions using cosine distance.
        """

        embedding_str = "[" + ",".join(map(str, embedding)) + "]"

        query = """
        SELECT
            transaction_id,
            content,
            1 - (embedding <=> %s::vector) AS similarity
        FROM transaction_embeddings
        WHERE user_id = %s
        ORDER BY embedding <=> %s::vector
        LIMIT %s
        """

        rows = self.execute_many(
            query,
            (
                embedding_str,
                user_id,
                embedding_str,
                top_k,
            ),
        )

        return [
            {
                "transaction_id": row[0],
                "content": row[1],
                "similarity": row[2],
            }
            for row in rows
        ]

    def delete_embedding(
        self,
        transaction_id: uuid.UUID,
    ):
        query = """
        DELETE FROM transaction_embeddings
        WHERE transaction_id = %s
        """

        self.execute(query, (transaction_id,))
