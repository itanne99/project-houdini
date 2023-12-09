from sqlmodel import SQLModel, Field
from typing import Optional
import json


class User(SQLModel, table=True):
  id: Optional[int] = Field(default=none, primary_key=True)
  firstName: str
  lastName: str
  email: str
  password: str #TODO: Needs to be encrypted
  active: bool
  guid: str
  createDate: Optional[datetime] = Field(default=datetime.utcnow())
  updateDate: Optional[datetime] = Field(default=datetime.utcnow())
  additionalInfo: str #TODO: Will be a json str