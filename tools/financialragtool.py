from agent_framework import tool
from services.RagService import RagService


@tool
async def financialragtool(question: str) -> str:
    """
    Retrieves financial transactions and provides spending insights.
    """
 
    ragservice = RagService()
   
    return await ragservice.ask(question)