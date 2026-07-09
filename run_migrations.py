
from pathlib import Path

from data_layer.connection import close_pool, run_migrations


def main() -> None:
    migrations_path = Path(__file__).resolve().parent / "migrations"
    run_migrations(migrations_path=migrations_path)
    close_pool()
    print("Database migrations completed.")


if __name__ == "__main__":
    main()
