from ..Model.note import Note
from ..Repository.note import NoteRepository
from ..schema import NoteInput, NoteType


class NoteService:

    @staticmethod
    async def add_note(note_data: NoteInput):
        await NoteRepository.create(note_data)

        return NoteType(id=note_data.id, name=note_data.name, description=note_data.description, createDate=note_data.createDate, updateDate=note_data.updateDate)

    @staticmethod
    async def get_all_note():
        list_note = await NoteRepository.get_all()
        return [NoteType(id=note.id, name=note.name, description=note.description, createDate=note.createDate, updateDate=note.updateDate) for note in list_note]

    @staticmethod
    async def get_by_id(note_id: int):
        note = await NoteRepository.get_by_id(note_id)
        return NoteType(id=note.id, name=note.name, description=note.description, createDate=note.createDate, updateDate=note.updateDate)

    @staticmethod
    async def delete(note_id: int):
        await NoteRepository.delete(note_id)
        return {'message': f'Successfully deleted data by id {note_id}'}

    @staticmethod
    async def update(note_id:int, note_data: NoteInput):
        await NoteRepository.update(note_id, note_data)
        return {'message': f'Successfully updated data by id {note_id}'}