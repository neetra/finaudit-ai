from agent_framework import tool
import pdfplumber
import pytesseract
from pdf2image import convert_from_path



@tool
async def parse_pdf(file_path: str) -> str:
    text_chunks = []
    print(f"Parsing PDF file: {file_path}")

    try:
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                # FIX: Use extract_text() instead of extract_tables() to get a string
                page_text = page.extract_text()

                if page_text and page_text.strip():
                    text_chunks.append(page_text)
                    print(f"--- Extracted digital text from Page {page_num} ---")
                else:
                    print(f"[Warning] Page {page_num} is empty/scanned. Falling back to OCR...")
                    ocr_text = ocr_page(file_path, page_num)
                    if ocr_text.strip():
                        text_chunks.append(ocr_text)
                        
    except Exception as exc:
        print(f"[Error] PDF parsing failed for {file_path}: {exc}")
        return ""

    final_text = "\n\n".join(text_chunks)
    print(f"---------------------------Final extracted text:\n{final_text}")
    return final_text


def ocr_page(file_path: str, page_num: int) -> str:
    """Converts a specific PDF page to an image and runs OCR."""
    try:
        # Paths specific to your environment
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        poppler_path = r"C:\Program Files\poppler-26.02.0\Library\bin"
        
        # FIX: Changed --psm 4 to --psm 6 (better for preserving table blocks)
        # Added preserve_interword_spaces to keep spacing between columns intact
        config = "--oem 3 --psm 6 -c preserve_interword_spaces=1"
        
        images = convert_from_path(
            file_path,
            first_page=page_num,
            last_page=page_num,
            dpi=300,
            poppler_path=poppler_path,
        )

        if images:
            extracted_text = pytesseract.image_to_string(images[0], config=config)
            print(f"--- Successfully OCR'd Page {page_num} ---")
            return extracted_text

    except Exception as exc:
        print(f"[Error] OCR failed on Page {page_num}: {exc}")

    return ""