'''
Pocket Miner - Inventory File
This file contains the Inventory class for Pocket Miner.
'''
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    def use_item(self, item):
        if item in self.items:
            # Perform the action associated with using the item
            pass