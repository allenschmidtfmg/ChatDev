'''
This file contains the Database class which handles the connection to the MongoDB database.
'''
from pymongo import MongoClient
class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['object_manager_db']
        self.objects_collection = self.db['objects']
        self.notes_collection = self.db['notes']
    def save_objects(self, objects):
        self.objects_collection.insert_many(objects)
    def load_objects(self):
        return list(self.objects_collection.find())
    def save_notes(self, notes):
        self.notes_collection.insert_many(notes)
    def load_notes(self):
        return list(self.notes_collection.find())