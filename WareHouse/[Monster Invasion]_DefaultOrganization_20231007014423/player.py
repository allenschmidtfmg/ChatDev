'''
This file contains the Player class, which represents the player character in the game.
'''
import tkinter as tk
class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = tk.PhotoImage(file="player.png")
        self.x = 400
        self.y = 550
        self.speed = 5
        self.direction = None
    def draw(self):
        self.canvas.create_image(self.x, self.y, image=self.image)
    def move_left(self):
        self.direction = "left"
    def move_right(self):
        self.direction = "right"
    def stop(self):
        self.direction = None
    def update(self):
        if self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed