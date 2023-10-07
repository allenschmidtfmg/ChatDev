'''
This file contains the Game class, which represents the game logic and GUI elements.
'''
import tkinter as tk
from player import Player
from monster import Monster
class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Monster Invasion")
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.player = Player(self.canvas)
        self.monsters = []
        self.canvas.bind("<KeyPress>", self.handle_keypress)
        self.canvas.bind("<KeyRelease>", self.handle_keyrelease)
        self.canvas.focus_set()
        self.is_running = False
    def start(self):
        self.is_running = True
        self.update()
    def update(self):
        if self.is_running:
            self.canvas.delete(tk.ALL)
            self.player.update()  # Update the player's position
            self.player.draw()
            for monster in self.monsters:
                monster.update()  # Update the monster's position
                monster.draw()
            self.root.after(16, self.update)
    def handle_keypress(self, event):
        if event.keysym == "Left":
            self.player.move_left()
        elif event.keysym == "Right":
            self.player.move_right()
    def handle_keyrelease(self, event):
        if event.keysym == "Left" or event.keysym == "Right":
            self.player.stop()
class Monster:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.image = tk.PhotoImage(file="monster.png")
        self.x = x
        self.y = y
        self.speed = 2
    def draw(self):
        self.canvas.create_image(self.x, self.y, image=self.image)
    def update(self):
        self.y += self.speed
player.py