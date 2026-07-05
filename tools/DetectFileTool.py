from pathlib import Path
from tools.BaseTool import BaseTool


class DetectFileTool(BaseTool):

    def __init__(self):
        super().__init__("File Type Detector Tool")

    async def execute(self, file_path):

        extension = Path(file_path).suffix.lower()

        return {
            "extension": extension,
            "is_csv": extension == ".csv",
            "is_pdf": extension == ".pdf",
            "is_image": extension in [".png", ".jpg", ".jpeg"]
        }