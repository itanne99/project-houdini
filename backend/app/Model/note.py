from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    createDate: Optional[datetime] = Field(default=datetime.utcnow())
    updateDate: Optional[datetime] = Field(default=datetime.utcnow())