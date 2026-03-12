import sys
try:
    from pypdf import PdfReader
    import docx

    def extract_pdf(pdf_path):
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        with open("resume_text.txt", "w", encoding="utf-8") as f:
            f.write(text)

    def extract_docx(docx_path):
        doc = docx.Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        with open("portfolio_text.txt", "w", encoding="utf-8") as f:
            f.write(text)

    extract_pdf("履歷ver8 20250930.docx.pdf")
    extract_docx("作品集.docx")
    print("Extraction successful.")
except Exception as e:
    print(f"Error: {e}")
