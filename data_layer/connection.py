from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from data_layer.config import get_database_settings
from data_layer.exceptions import DatabaseDependencyError

try:
    import psycopg2
    from psycopg2 import pool
except ImportError:
    psycopg2 = None
    pool = None


_pool = None


def init_pool(min_connections: int | None = None, max_connections: int | None = None):
    """Initialize the PostgreSQL connection pool."""
    global _pool

    if _pool is not None:
        return _pool

    if pool is None:
        raise DatabaseDependencyError(
            "psycopg2 is required for database operations. Install dependencies with `pip install -r requirements.txt`."
        )

    settings = get_database_settings()
    _pool = pool.SimpleConnectionPool(
        min_connections or settings.min_connections,
        max_connections or settings.max_connections,
        dsn=settings.url,
    )
    return _pool


@contextmanager
def get_connection() -> Iterator:
    """Yield a pooled database connection and return it to the pool."""
    connection_pool = init_pool()
    connection = connection_pool.getconn()
    try:
        yield connection
    finally:
        connection_pool.putconn(connection)


@contextmanager
def transaction() -> Iterator:
    """Run operations in a database transaction."""
    with get_connection() as connection:
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise


def close_pool() -> None:
    global _pool

    if _pool is not None:
        _pool.closeall()
        _pool = None


def run_migrations(migrations_path: Path | None = None) -> None:
    """Execute SQL migration files in filename order."""
    if psycopg2 is None:
        raise DatabaseDependencyError(
            "psycopg2 is required for database migrations. Install dependencies with `pip install -r requirements.txt`."
        )

    path = Path(__file__).parent / "scripts" / "migrations"
    sql_files = sorted(path.glob("*.sql"))

    print(f"Running migrations from {path}")
    print(f"Executing migration files from {path}")
    with transaction() as connection:
        with connection.cursor() as cursor:
            for sql_file in sql_files:
                print(f"Executing migration file: {sql_file}")
                cursor.execute(sql_file.read_text(encoding="utf-8"))


def initialize_database() -> None:
    """Run migrations and create stored procedures/functions used by the data layer."""
    from data_layer.scripts.run_functions import create_database_functions

    run_migrations()
    create_database_functions()
