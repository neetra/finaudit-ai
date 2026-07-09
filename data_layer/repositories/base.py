from typing import Any, Sequence

from data_layer.connection import transaction


class BaseRepository:
    def execute_one(self, query: str, params: Sequence[Any] = ()) -> tuple | None:
        with transaction() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()

    def execute_many(self, query: str, params: Sequence[Any] = ()) -> list[tuple]:
        with transaction() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()

    def execute(self, query: str, params: Sequence[Any] = ()) -> None:
        with transaction() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
