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

@strawberry.input
class UserType:
    id: int
    firstName: str
    lastName: str
    email: str
    password: str
    active: bool
    guid: str
    createDate: datetime
    updateDate: datetime
    additionalInfo: str

@strawberry.input
class CreateUserInput:
    firstName: str
    lastName: str
    email: str
    password: str
    additionalInfo: str

@strawberry.input
class UpdateUserInput:
    firstName: str
    lastName: str
    email: str
    additionalInfo: str