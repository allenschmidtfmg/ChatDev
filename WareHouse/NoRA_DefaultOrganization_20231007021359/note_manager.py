'''
This file contains the NoteManager class which handles the management of notes.
'''
from database import Database
class NoteManager:
    def __init__(self):
        self.notes = []
        self.database = Database()
    def get_notes(self):
        return self.notes
    def set_notes(self, notes):
        self.notes = notes
    def add_note(self, note):
        self.notes.append(note)
    def delete_note(self, note):
        self.notes.remove(note)
    def save_notes(self):
        self.database.save_notes(self.notes)
    def load_notes(self):
        self.notes = self.database.load_notes()