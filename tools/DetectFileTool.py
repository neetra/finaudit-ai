# tools/detect_file_tool.py

from pathlib import Path

from agent_framework import tool



@tool
def detect_file(file_path: str):

    suffix = Path(file_path).suffix.lower()

    return {
        "extension": suffix,
        "is_pdf": suffix == ".pdf",
        "is_csv": suffix == ".csv"
    }