import pandas as pd
import fitz  # PyMuPDF

def extract_excel(file):
    """Extracts and returns data from an Excel file."""
    return pd.read_excel(file)

def extract_pdf_text(file):
    """Extracts and returns text from a PDF file."""
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text
