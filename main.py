from fastapi import FastAPI, UploadFile, File, Request
from document_loader import load_and_chunk_document
from embed_store import embed_and_store
from query_handler import generate_answer

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    chunks = await load_and_chunk_document(file)
    embed_and_store(chunks)
    return {"message": "File processed", "chunks_stored": len(chunks)}

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    question = data.get("question", "")
    result = await generate_answer(question)
    return result
