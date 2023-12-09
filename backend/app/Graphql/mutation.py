import strawberry
from ..Service.note import NoteService
from ..schema import NoteType, NoteInput, UserType, UpdateUserInput, CreateUserInput


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_note(self, note_data: NoteInput) -> NoteType:
        return await NoteService.add_note(note_data)

    @strawberry.mutation
    async def delete_note(self, note_id: int) -> str:
        return await NoteService.delete(note_id)

    @strawberry.mutation
    async def update_note(self, note_id: int, note_data: NoteInput) -> str:
        return await NoteService.update(note_id,note_data)

    @strawberry.mutation
    def create_user(user_data: CreateUserInput) -> UserType:
        return await UserService.create_user(user_data)

    @strawberry.mutation
    def delete_user(user_guid: str) -> dict:
        return await UserService.delete(user_guid)

    @strawberry.mutation
    def activate_user(user_guid: str) -> dict:
        return await UserService.activate(user_guid)

    @strawberry.mutation
    def deactivate_user(user_guid: str) -> dict:
        return await UserService.deactivate(user_guid)

    @strawberry.mutation
    def update_user(user_guid: str, user_data: UpdateUserInput) -> dict:
        return await UserService.update(user_guid, user_data)

    @strawberry.mutation
    def update_user_password(user_guid: str, password: str) -> dict:
        return await UserService.update(user_guid, password)