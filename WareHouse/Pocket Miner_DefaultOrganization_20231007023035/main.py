'''
Pocket Miner - Main File
'''
import tkinter as tk
from game import Game, StoreWindow  # Import the StoreWindow class
class PocketMinerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pocket Miner")
        self.geometry("800x600")
        self.resizable(False, False)
        self.game = Game(self)
        self.game.pack()
if __name__ == "__main__":
    app = PocketMinerApp()
    app.mainloop()