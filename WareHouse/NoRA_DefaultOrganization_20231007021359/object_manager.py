'''
This file contains the ObjectManager class which handles the management of objects.
'''
from database import Database
class ObjectManager:
    def __init__(self):
        self.objects = []
        self.database = Database()
    def get_objects(self):
        return self.objects
    def set_objects(self, objects):
        self.objects = objects
    def add_object(self, obj):
        self.objects.append(obj)
    def delete_object(self, obj):
        self.objects.remove(obj)
    def save_objects(self):
        self.database.save_objects(self.objects)
    def load_objects(self):
        self.objects = self.database.load_objects()