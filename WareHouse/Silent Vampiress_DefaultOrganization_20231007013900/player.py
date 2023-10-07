'''
This file contains the PlayerInfo class which represents a player in the game.
'''
import random
class PlayerInfo:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def take_turn(self):
        print(f"It's {self.name}'s turn.")
        input("Press enter to roll the dice...")
        dice_roll = random.randint(1, 6)
        print(f"{self.name} rolled a {dice_roll}.")
        self.score += dice_roll
    def is_winner(self):
        return self.score >= 50