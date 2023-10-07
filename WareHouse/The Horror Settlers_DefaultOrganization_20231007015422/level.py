'''
This file contains the Level class that manages the game levels.
'''
class Level:
    def __init__(self):
        self.current_level = 1
    def increase_level(self):
        # Increase the current level
        self.current_level += 1