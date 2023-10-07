'''
Monster Invasion - Game File
This file contains the Game class that manages the game logic.
'''
import random
class Game:
    def __init__(self):
        self.canvas = None
        self.monsters = []
        self.score = 0
    def start(self, canvas):
        self.canvas = canvas
        self.canvas.bind("<Button-1>", self.on_click)
        self.spawn_monster()
        self.update()
    def spawn_monster(self):
        # Spawn a new monster at a random position
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        self.monsters.append((x, y))
    def on_click(self, event):
        # Check if the click is on a monster
        for monster in self.monsters:
            if abs(event.x - monster[0]) < 50 and abs(event.y - monster[1]) < 50:
                self.monsters.remove(monster)
                self.score += 1
    def update(self):
        # Clear the canvas
        self.canvas.delete("all")
        # Draw the monsters
        for monster in self.monsters:
            x, y = monster
            self.canvas.create_oval(x-25, y-25, x+25, y+25, fill="red")
        # Draw the score
        self.canvas.create_text(50, 50, text=f"Score: {self.score}", anchor="nw", font=("Arial", 16))
        # Schedule the next update
        self.canvas.after(1000, self.update)
        # Remove defeated monsters
        self.monsters = [monster for monster in self.monsters if not self.is_defeated(monster)]
        # Update the score
        self.score += len(self.monsters)
    def is_defeated(self, monster):
        # Check if a monster is defeated
        x, y = monster
        return abs(x - self.canvas.winfo_pointerx()) < 50 and abs(y - self.canvas.winfo_pointery()) < 50