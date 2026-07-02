import os
from pathlib import Path

from dotenv import load_dotenv

from orm_agent import FinancialORMAgent

ENV_PATH = Path(__file__).parent / ".env"
LOCAL_ENV_PATH = Path(__file__).parent / ".localenv"


def load_configuration():
    load_dotenv(dotenv_path=ENV_PATH, override=False)
    load_dotenv(dotenv_path=LOCAL_ENV_PATH, override=True)

    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
    }


def main():
    config = load_configuration()
    agent = FinancialORMAgent(database_url=config["DATABASE_URL"])
    agent.create_schema()

    print("Financial AI agent scaffold is ready.")
    print("Loaded configuration:")
    print(f"  OPENAI_API_KEY set: {bool(config['OPENAI_API_KEY'])}")
    print(f"  DATABASE_URL: {config['DATABASE_URL']}")
    print(f"  LOG_LEVEL: {config['LOG_LEVEL']}")


if __name__ == "__main__":
    main()
