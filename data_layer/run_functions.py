from pathlib import Path

from connection import transaction


def create_database_functions() -> None:
    sql_path = Path(__file__).resolve().parent / "migrations" / "003_functions.sql"
    if not sql_path.exists():
        raise FileNotFoundError(f"Database functions SQL file not found: {sql_path}")

    with transaction() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql_path.read_text(encoding="utf-8"))


def main() -> None:
    create_database_functions()
    print("Database functions initialized.")


if __name__ == "__main__":
    main()
