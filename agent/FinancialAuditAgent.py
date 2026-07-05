import asyncio
import json

from agent.agent import BaseAgent
from tools.ToolExecutor import ToolExecutor
from tools.DetectFileTool import DetectFileTool
from tools.CsvParserTool import CsvParserTool
from tools.PdfParserTool import PdfParserTool
from tools.TransactionExtractorTool import TransactionExtractorTool


class FinancialAuditAgent(BaseAgent):
    """Financial audit agent for document and transaction analysis."""

    def __init__(self, model_provider: str, agent_name: str = "financial_audit_agent", instructions: str = None, tools: list = None):
        super().__init__(model_provider=model_provider, agent_name=agent_name, instructions=instructions, tools=tools)
        llm = self.llm
        self.tool_executor = ToolExecutor({
            "detect_file": DetectFileTool(),
            "csv_parser": CsvParserTool(),
            "pdf_parser": PdfParserTool(),
            "transaction_extractor": TransactionExtractorTool(llm),
        })

    def process(self, user_input: str):
        return self.run(user_input)

    def process_document(self, file_path: str):
        file_info = asyncio.run(self.tool_executor.execute("detect_file", file_path=file_path))

        if file_info.get("is_csv"):
            data = asyncio.run(self.tool_executor.execute("csv_parser", file_path=file_path))
        elif file_info.get("is_pdf"):
            data = asyncio.run(self.tool_executor.execute("pdf_parser", file_path=file_path))
        else:
            return {
                "file_path": file_path,
                "status": "unsupported_format",
            }

        transactions = asyncio.run(
            self.tool_executor.execute("transaction_extractor", statement_text=data)
        )

        return {
            "file_path": file_path,
            "file_type": "csv" if file_info.get("is_csv") else "pdf",
            "transactions": json.loads(transactions),
        }