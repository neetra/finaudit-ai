from agent_framework import tool

def create_extraction_tool(llm):
    """Factory that injects the LLM dependency in the background."""
    
    @tool
    def extract_transactions(statement_text: str) -> str:
        """
        Extracts every financial transaction from a raw bank statement string.
        
        Args:
            statement_text: The full string text or markdown of the bank statement.
        """
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

        Bank Statement: {statement_text}
        """
        # Uses the llm from the outer scope seamlessly
        response = llm.generate(prompt)
        return response

    return extract_transactions