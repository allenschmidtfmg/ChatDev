'''
Monster Invasion - Main File
This file contains the main entry point for the Monster Invasion game.
'''
import tkinter as tk
from game import Game
def main():
    # Create the game instance
    game = Game()
    # Create the main window
    window = tk.Tk()
    window.title("Monster Invasion")
    # Set up the game canvas
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack()
    # Start the game loop
    game.start(canvas)
    # Run the main tkinter event loop
    window.mainloop()
if __name__ == "__main__":
    main()