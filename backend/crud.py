from sqlalchemy.orm import Session
from . import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_document(db: Session, filename: str, filepath: str):
    document = models.Document(id=str(uuid4()), filename=filename, filepath=filepath)
    db.add(document)
    db.commit()
    db.refresh(document)
    return document

def get_document(db: Session, document_id: str):
    return db.query(models.Document).filter(models.Document.id == document_id).first()
