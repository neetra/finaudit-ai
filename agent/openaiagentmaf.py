import os

from agent_framework import Agent

from agent_framework.foundry import FoundryChatClient

from azure.identity import DefaultAzureCredential
import dotenv
from azure.core.credentials import AzureKeyCredential
from tools import TOOLS

class openaiagentmaf:
    def __init__(self):
        dotenv.load_dotenv(dotenv.find_dotenv())

        endpoint = os.getenv("FOUNDRY_ENDPOINT")
        deployment_name = os.getenv("AZURE_OPENAI_MODEL")
      
        print(f"Endpoint: {endpoint}")
        print(f"Deployment Name: {deployment_name}")
        self.client = FoundryChatClient(
        project_endpoint=endpoint,
        model=deployment_name,
        credential=DefaultAzureCredential()
)  

       

        # 3. Create the Agent with its tool registry
        self.agent = Agent(
            client=self.client,
            name="FinancialAuditor",
            instructions="""You analyze bank statements.

Workflow

1. Detect file.
2. Parse file.3. 
3. Extract transactions.
4. Return JSON in strictly below format

""",
    tools=TOOLS
        )

    def get_agent(self):
        return self.agent
