'''
Pocket Miner - Main File
This file contains the main logic and GUI implementation for the Pocket Miner game.
'''
import tkinter as tk
from game import Game
class PocketMinerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pocket Miner")
        self.geometry("800x600")
        self.resizable(False, False)
        self.game = Game()
        self.create_widgets()
    def create_widgets(self):
        # Create and place GUI elements here
        start_button = tk.Button(self, text="Start Game", command=self.start_game)
        start_button.pack()
        quit_button = tk.Button(self, text="Quit", command=self.quit)
        quit_button.pack()
        # Bind key press events to handle user input
        self.bind("<Key>", self.handle_input)
    def start_game(self):
        self.game.start_game()
    def handle_input(self, event):
        self.game.handle_input(event)
if __name__ == "__main__":
    app = PocketMinerApp()
    app.mainloop()