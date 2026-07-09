from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: Optional[str]
    email: str
    name: Optional[str] = None
    password: Optional[str] = None
    created_at: Optional[datetime] = None
