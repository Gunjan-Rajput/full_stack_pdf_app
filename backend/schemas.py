from pydantic import BaseModel
from datetime import datetime

class Document(BaseModel):
    id: str
    filename: str
    upload_date: datetime

    class Config:
        orm_mode = True
