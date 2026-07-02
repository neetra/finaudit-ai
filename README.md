# Financial AI Agent

Scaffold for a financial AI assistant that includes configuration loading, ORM schema support, and test input artifacts.

## Files

- `main.py`: entrypoint that loads environment configuration and initializes the ORM agent.
- `orm_agent.py`: SQLAlchemy-based agent with a `Transaction` model.
- `.env`: default environment variables.
- `.localenv`: local overrides for development.
- `test_input_files/`: sample bank and credit card statement files for parsing tests.
