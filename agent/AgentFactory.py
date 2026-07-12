import os

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from agent_framework.ollama import OllamaChatClient
from azure.identity import DefaultAzureCredential

from tools import TOOLS


class AgentFactory:
       


    
    def create_agent(self, model_provider: str = "foundry", agent_name: str = "FinancialAuditor", instructions: str | None = None, tools=None):
        if model_provider == "foundry":
            client = self._create_foundry_client()
        elif model_provider == "ollama":
            client = self._create_ollama_client()
        else:
            raise ValueError("Unsupported model provider. Use 'foundry' or 'ollama'.")

        agent_tools = tools if tools is not None else TOOLS
        agent_instructions = instructions or """
You are FinancialAuditor AI. You analyze bank statements and answer financial questions.

You have access to these tools:

1. detect_file:
   - Detects uploaded financial documents.

2. parse_pdf:
   - Extracts text from PDF bank statements.

3. parse_csv:
   - Extracts transaction data from CSV files.

4. extract_tool:
   - Converts raw extracted text into structured transaction JSON.

5. financial_rag_tool:
   - Retrieves stored transaction data and answers financial questions.
   - Use this tool for any question requiring historical transaction lookup,
     spending analysis, summaries, trends, or user-specific financial insights.

Workflow rules:

A. When a user uploads a bank statement:
   1. Detect the file.
   2. Parse the document.
   3. Extract transactions.
   4. Store transaction data.

B. When a user asks questions about financial data:
   Examples:
   - "What is my total spending?"
   - "How much did user123 spend?"
   - "Show my food expenses."
   - "What are my biggest expenses?"
   - "Summarize my transactions."

   Always call financial_rag_tool first.

C. Do not try to answer financial questions from memory.
   Always retrieve transaction data using available tools.

Return concise answers with numbers and explanations.
"""

        return Agent(
            client=client,
            name=agent_name or "FinancialAuditor",
            instructions=agent_instructions,
            tools=agent_tools,
        )

    def _create_foundry_client(self):
        endpoint = os.getenv("FOUNDRY_ENDPOINT")
        deployment_name = os.getenv("AZURE_OPENAI_MODEL") 

        if not endpoint:
            raise ValueError("FOUNDRY_ENDPOINT or FOUNDRY_PROJECT_ENDPOINT is required for Foundry mode.")
        if not deployment_name:
            raise ValueError("AZURE_OPENAI_MODEL or AZURE_OPENAI_DEPLOYMENT is required for Foundry mode.")

        return FoundryChatClient(
            project_endpoint=endpoint,
            model=deployment_name,
            credential=DefaultAzureCredential(),
        )

    def _create_ollama_client(self):
        model_name = os.getenv("OLLAMA_MODEL", "gemma4")
        return OllamaChatClient(model=model_name)
