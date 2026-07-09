from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Optional


@dataclass
class Transaction:
    id: Optional[int]
    user_id: int
    date: date
    type: str
    amount: Decimal
    currency: str = "USD"
    description: Optional[str] = None
    merchant: Optional[str] = None
    category: Optional[str] = None
    created_at: Optional[datetime] = None
