import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class DatabaseSettings:
    host: str
    port: int
    username: str
    password: str
    database: str
    url: str
    min_connections: int = 1
    max_connections: int = 10


def get_database_settings() -> DatabaseSettings:
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "5432"))
    username = os.getenv("DB_USERNAME", "postgres")
    password = os.getenv("DB_PASSWORD", "postgres")
    database = os.getenv("DB_NAME", "finaudit")

    url = os.getenv("DATABASE_URL") or f"postgresql://{username}:{password}@{host}:{port}/{database}"

    return DatabaseSettings(
        host=host,
        port=port,
        username=username,
        password=password,
        database=database,
        url=url,
        min_connections=int(os.getenv("DB_MIN_CONNECTIONS", "1")),
        max_connections=int(os.getenv("DB_MAX_CONNECTIONS", "10")),
    )
