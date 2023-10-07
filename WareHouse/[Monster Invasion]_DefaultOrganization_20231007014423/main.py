'''
This is the main file of the Monster Invasion software. It contains the main function that initializes the GUI and starts the application.
'''
import tkinter as tk
from game import Game
def main():
    root = tk.Tk()
    game = Game(root)
    game.start()
    root.mainloop()
if __name__ == "__main__":
    main()