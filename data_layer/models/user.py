from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class User:
    id: Optional[UUID]
    email: str
    name: Optional[str] = None
    password: Optional[str] = None
    created_at: Optional[datetime] = None
