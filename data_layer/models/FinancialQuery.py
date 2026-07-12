from dataclasses import dataclass
from datetime import date
from typing import Optional
from uuid import UUID


@dataclass
class FinancialQuery:
    user_id: str
    question: str

    # Optional filters
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    merchant: Optional[str] = None
    category: Optional[str] = None