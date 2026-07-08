from agent_framework import Agent
from agent_framework.ollama import OllamaChatClient

from tools import TOOLS

class ollamaaiagentmaf:
    def __init__(self, model_name = "gemma4"):
        self.client = OllamaChatClient(model=model_name)

   
    
    # 2. Define the core System Prompt for extraction & classification
        financial_instructions = """
        You are the core intelligence of finaudit.ai. Your objective is to extract, clean, 
        categorize, and save bank transactions.
        
        Follow this execution loop:
        1. Check the file extension provided by the user. Invoke the appropriate parser tool (`parse_pdf_statement` or `parse_csv_statement`).
        2. Review the raw transaction data returned. Clean up the descriptions.
        3. Categorize each transaction into standard buckets (e.g., Groceries, Income, Utilities, Entertainment, Savings).
        4. Format the final output into a validated JSON object with two top-level keys: "expenses" and "savings".
        5. Pass that exact structured JSON payload to `save_transactions_to_db` to persist the data.
        6. Return the structured JSON to the user as your final text response.
        """

        # 3. Create the Agent with its tool registry
        self.agent = Agent(
            client=self.client,
            name="FinancialAuditor",
            instructions="""You analyze bank statements.

Workflow

1. Detect file.
2. Parse file.
3. Extract transactions.
4. Return JSON.
""",
    tools=TOOLS
        )

    def get_agent(self):
        return self.agent

    
    def get_client(self):
        return self.client