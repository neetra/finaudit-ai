from providers.base import BaseLLM
from tools.BaseTool import BaseTool


class TransactionExtractorTool(BaseTool):

    name = "transaction_extractor"

    description = "Extract bank transactions."

    def __init__(self, llm : BaseLLM):
        super().__init__("Transaction Extractor Tool")
        self.llm = llm

    async def execute(self, statement_text):

        prompt = f"""
               Instructions:
- Extract every transaction.
- Return ONLY valid JSON.
- Do not include markdown, code fences, explanations, or additional text.
- If a field is missing, use null.

- Infer the transaction category when possible, otherwise use null.
- Detect the transaction type as either "credit" or "debit".
- Preserve the original transaction description.
- Detect the currency if present; otherwise use USD.
Return JSON in exactly this format:

{{
  "transactions": [
    {{
      "date": "YYYY-MM-DD",
      "type": "credit",
      "amount": 1500.00,
      "currency": "USD",
      "description": "Salary Deposit",
      "category": "Income"
    }}
  ]
}}

Bank Statement:

{statement_text}
"""
        
        response = self.llm.generate(prompt)
        return response