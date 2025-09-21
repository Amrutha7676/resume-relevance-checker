import docx
from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    """Extract text from a PDF file."""
    reader = PdfReader(file)
    return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

def extract_text_from_docx(file):
    """Extract text from a DOCX file."""
    doc = docx.Document(file)
    return " ".join([para.text for para in doc.paragraphs])
def extract_text_from_file(file):
    if file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":  # docx
        return extract_text_from_docx(file)
    elif file.type == "application/pdf":
        return extract_text_from_pdf(file)
    elif file.type == "text/plain":
        return str(file.read(), "utf-8")
    else:
        return ""

