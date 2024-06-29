from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
import fitz  # PyMuPDF
from pydantic import BaseModel
from sqlalchemy.orm import Session
from uuid import uuid4
import os

from .database import SessionLocal, engine
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.post("/upload", response_model=schemas.Document)
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(crud.get_db)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type")

    file_id = str(uuid4())
    file_location = f"{UPLOAD_DIR}/{file_id}.pdf"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    text = extract_text_from_pdf(file_location)
    document = crud.create_document(db, file.filename, file_location)
    return document

class QuestionRequest(BaseModel):
    document_id: str
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest, db: Session = Depends(crud.get_db)):
    document = crud.get_document(db, request.document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    text = extract_text_from_pdf(document.filepath)
    answer = f"Mock answer for the question: '{request.question}' based on the document content."
    return JSONResponse(content={"answer": answer})
