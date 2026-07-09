# Data Layer

This package owns database access for the financial agent.

## Structure

- `config.py`: database configuration loaded from environment variables.
- `connection.py`: PostgreSQL connection pool, transaction context, and migration runner.
- `models/`: dataclasses representing database records.
- `repositories/`: database operations grouped by domain.
- `migrations/`: SQL schema and database helper scripts.
- `scripts/`: runnable helpers such as migration execution.

## Environment

Set `DATABASE_URL` in `.env`.

Example:

```text
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/finaudit
DB_MIN_CONNECTIONS=1
DB_MAX_CONNECTIONS=10
```

## Run Migrations

```powershell
python -m data_layer.scripts.run_migrations
```
