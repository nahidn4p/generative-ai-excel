import pdfplumber, pytesseract, docx, io
from PIL import Image

async def load_and_chunk_document(file):
    ext = file.filename.lower().split('.')[-1]
    content = []

    if ext == "pdf":
        content = extract_text_from_pdf(await file.read())
    elif ext == "docx":
        content = extract_text_from_docx(await file.read())
    elif ext in ["jpg", "jpeg", "png"]:
        content = extract_text_from_image(await file.read())
    elif ext == "txt":
        content = [line.decode() for line in file.file.readlines()]
    else:
        content = ["Unsupported format"]

    return [chunk.strip() for chunk in content if chunk.strip()]

def extract_text_from_pdf(raw_bytes):
    chunks = []
    with pdfplumber.open(io.BytesIO(raw_bytes)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                chunks.append(text)
    return chunks

def extract_text_from_docx(raw_bytes):
    doc = docx.Document(io.BytesIO(raw_bytes))
    return [para.text for para in doc.paragraphs if para.text.strip()]

def extract_text_from_image(raw_bytes):
    image = Image.open(io.BytesIO(raw_bytes))
    text = pytesseract.image_to_string(image)
    return [text]
