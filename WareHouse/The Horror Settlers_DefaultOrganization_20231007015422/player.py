'''
This file contains the Player class that represents the player character.
'''
class Player:
    def __init__(self):
        self.level = 1
        self.experience = 0
    def level_up(self):
        # Increase the player's level
        self.level += 1
    def gain_experience(self, amount):
        # Increase the player's experience
        self.experience += amount