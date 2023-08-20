import json
import Note
import datetime

class NotesManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                for note_data in data:
                    note = Note.Note(note_data['id'], note_data['title'], note_data['body'])
                    note.created_at = datetime.datetime.strptime(note_data['created_at'], '%Y-%m-%d %H:%M:%S.%f')
                    note.updated_at = datetime.datetime.strptime(note_data['updated_at'], '%Y-%m-%d %H:%M:%S.%f')
                    self.notes.append(note)
        except FileNotFoundError:
            pass

    def save_notes(self):
        data = [note.to_dict() for note in self.notes]
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

    def add_note(self, title, body):
        id = len(self.notes) + 1
        note = Note.Note(id, title, body)
        self.notes.append(note)
        return note

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def update_note_by_id(self, id, title=None, body=None):
        note = self.get_note_by_id(id)
        if note is not None:
            note.update(title=title, body=body)

    def delete_note_by_id(self, id):
        note = self.get_note_by_id(id)
        if note is not None:
            self.notes.remove(note)