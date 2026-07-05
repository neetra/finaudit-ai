import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from tools.BaseTool import BaseTool


class PdfParserTool(BaseTool):

    def __init__(self):
        super().__init__("PDF Parser Tool")

    async def execute(self, file_path):
        text = ""
        print(f"Parsing using {self.name} file: {file_path}")

        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                # Try standard text extraction first
                page_text = page.extract_text(layout=True)

                if page_text and page_text.strip():
                    text += page_text + "\n"
                    print(
                        f"--- Extracted digital text from Page {page_num} ---"
                    )
                else:
                    # Fallback to OCR if digital text is empty
                    print(
                        f"[Warning] Page {page_num} is empty/scanned. Falling back to OCR..."
                    )
                    ocr_text = self._ocr_page(file_path, page_num)
                    text += ocr_text + "\n"

        return text

    def _ocr_page(self, file_path, page_num):
        """Converts a specific PDF page to an image and runs OCR."""
        try:
            # 1. Point pytesseract directly to the installed OCR binary
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

            # 2. Your existing Poppler path setup
            POPPLER_PATH = r"C:\Program Files\poppler-26.02.0\Library\bin"

            images = convert_from_path(
                file_path,
                first_page=page_num,
                last_page=page_num,
                dpi=300,
                poppler_path=POPPLER_PATH
            )
            
            if images:
                extracted_text = pytesseract.image_to_string(images[0])
                print(f"--- Successfully OCR'd Page {page_num} ---")
                return extracted_text
                
        except Exception as e:
            print(f"[Error] OCR failed on Page {page_num}: {e}")

        return ""