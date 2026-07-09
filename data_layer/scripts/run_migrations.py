
from pathlib import Path

from data_layer.connection import close_pool, run_migrations


def main() -> None:
   
    run_migrations()
    close_pool()
    print("Database migrations completed.")


if __name__ == "__main__":
    main()
