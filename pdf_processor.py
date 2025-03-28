from pypdf import PdfReader
from io import BytesIO

def extract_text_from_pdf(pdf_data: bytes) -> str:
    """
    Extract text from the first page of a PDF.

    Args:
        pdf_data: Raw bytes of the PDF file

    Returns:
        The extracted text from the first page
    """
    pdf_file = BytesIO(pdf_data)
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text.strip()


def count_pages(pdf_data: bytes) -> int:
    """
    Count the number of pages in a PDF.

    Args:
        pdf_data: Raw bytes of the PDF file

    Returns:
        The number of pages
    """
    pdf_file = BytesIO(pdf_data)
    reader = PdfReader(pdf_file)
    return len(reader.pages)


def extract_text_from_pdfimage(image_data: bytes) -> str:
    """
    Extract text from an image using OCR.

    Args:
        image_data: Raw bytes of the image file

    Returns:
        The extracted text from the image
    """
    # TODO: Implement OCR text extraction from image