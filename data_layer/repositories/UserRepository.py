from data_layer.models.user import User
from data_layer.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def create(self, email: str, name: str | None = None, password: str | None = None) -> str:
        row = self.execute_one(
            "SELECT create_user(%s, %s, %s)",
            (email, name, password),
        )
        return row[0]

    def get_by_id(self, user_id: str) -> User | None:
        row = self.execute_one(
            "SELECT id, email, name,  created_at FROM users WHERE id = %s",
            (user_id,),
        )
        return User(*row) if row else None

    def get_by_email(self, email: str) -> User | None:
        row = self.execute_one(
            "SELECT id, email, name, created_at FROM users WHERE email = %s",
            (email,),
        )
        return User(*row) if row else None
