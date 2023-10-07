'''
This is the main file of the erotic game application.
'''
import tkinter as tk
from game import Game
class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Erotic Game")
        self.geometry("800x600")
        self.game = Game()
        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.pack()
    def start_game(self):
        self.game.start()
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()