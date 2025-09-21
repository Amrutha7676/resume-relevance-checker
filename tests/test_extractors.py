from modules.extractors import extract_text_from_pdf, extract_text_from_docx

def test_pdf_extraction():
    assert callable(extract_text_from_pdf)

def test_docx_extraction():
    assert callable(extract_text_from_docx)
