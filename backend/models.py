from sqlalchemy import Column, String, DateTime
import datetime
from .database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(String, primary_key=True, index=True)
    filename = Column(String, index=True)
    filepath = Column(String)
    upload_date = Column(DateTime, default=datetime.datetime.utcnow)
