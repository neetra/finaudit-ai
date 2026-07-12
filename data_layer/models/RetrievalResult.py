from dataclasses import dataclass

@dataclass
class RetrievalResult:
    question: str
    transactions: list