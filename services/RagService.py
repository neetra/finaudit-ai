from services.QueryParser import QueryParser
from services.retrieval.TransactionRetriever import TransactionRetriever
from services.prompt.prompt_builder import PromptBuilder
from providers.llmfactory import LLMFactory


class RagService:

    def __init__(self):
        self.query_parser = QueryParser()
        self.retriever = TransactionRetriever()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMFactory.create("azureopenai")

    async def ask(self, question: str):

        financial_query = await self.query_parser.parse(question)

        retrieval =  self.retriever.retrieve(financial_query)

        prompt = self.prompt_builder.build(
            financial_query.question,
            retrieval,
        )

      
        return self.llm.generate(prompt)