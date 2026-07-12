from datetime import date
import json
from uuid import UUID

from data_layer.models import FinancialQuery
from providers.llmfactory import LLMFactory


class QueryParser:

    def __init__(self):
        self.llm = LLMFactory.create("azureopenai")

    async def parse(self, question: str) -> FinancialQuery:
        prompt = f"""
Extract the following from the user's question.

Return JSON only in .


{{
  "user_id": "",
  "question": "",
  "merchant": null,
  "category": null,
  "start_date": null,
  "end_date": null
}}

Question:
{question}
"""

        response = self.llm.generate(prompt)
        data = json.loads(response)

       

        financialQuery =  FinancialQuery(
            user_id=data["user_id"],
            question=data["question"],
            merchant=data.get("merchant"),
            category=data.get("category"),
            start_date=date.fromisoformat(data["start_date"]) if data.get("start_date") else None,
            end_date=date.fromisoformat(data["end_date"]) if data.get("end_date") else None,
)
        
        print(f"--------------------In query parser----------------------")
        return financialQuery