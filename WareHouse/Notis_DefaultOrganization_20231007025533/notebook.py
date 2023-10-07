'''
This file contains the Notebook class for managing notebooks in the Notion clone software.
'''
from note import Note
class Notebook:
    def __init__(self):
        self.notes = []
    def add_note(self, note):
        self.notes.append(note)
    def remove_note(self, note):
        self.notes.remove(note)
    def get_notes(self):
        return self.notes