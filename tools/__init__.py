# tools/__init__.py

from providers.llmfactory import LLMFactory

from .DetectFileTool import detect_file
from .CsvParserTool import parse_csv
from .PdfParserTool import parse_pdf
from .TransactionExtractorTool import create_extraction_tool
from .financialragtool import financialragtool


azureopenai = LLMFactory.create("azureopenai")
extract_tool = create_extraction_tool(azureopenai)

TOOLS = [
    detect_file,
    parse_pdf,
    parse_csv,
    extract_tool,
    financialragtool
]