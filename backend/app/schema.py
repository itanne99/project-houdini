import strawberry
from datetime import datetime

@strawberry.type
class NoteType:
    id: int
    name: str
    description: str
    createDate: datetime
    updateDate: datetime


@strawberry.input
class NoteInput:
    name: str
    description: str