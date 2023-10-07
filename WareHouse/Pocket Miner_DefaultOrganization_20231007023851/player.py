'''
Pocket Miner - Player File
This file contains the Player class for Pocket Miner.
'''
class Player:
    def __init__(self):
        # Initialize player variables here
        self.position = (0, 0)
    def update(self):
        # Update player position and state
        pass
    def move(self, direction):
        # Move the player in the specified direction
        if direction == "up":
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "down":
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "left":
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == "right":
            self.position = (self.position[0] + 1, self.position[1])