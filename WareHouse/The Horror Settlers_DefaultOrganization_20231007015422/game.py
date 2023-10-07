'''
This file contains the Game class that manages the game logic.
'''
import tkinter as tk
from player import Player
from level import Level
from quest import Quest
class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Horror Game")
        self.player = Player()
        self.level = Level()
        self.quest = Quest()
    def start(self):
        # Initialize the game UI
        self.create_ui()
        # Start the game loop
        self.game_loop()
    def create_ui(self):
        # Create and layout the UI elements
        self.level_label = tk.Label(self.root, text="Level: {}".format(self.player.level))
        self.level_label.pack()
    def game_loop(self):
        # Main game loop
        while self.player.level < 100:
            # Check if the active quest is completed
            if self.quest.check_quest_completion():
                # Reward the player upon quest completion
                self.quest.reward_player()
            # Increase the current level
            self.level.increase_level()
            # Generate a new quest for the player
            self.quest.generate_quest()
            # Start a new quest
            self.quest.start_quest()
            # Complete the active quest
            self.quest.complete_quest()
            # Increase the player's experience
            self.player.gain_experience(100)
            # Increase the player's level
            self.player.level_up()
            # Update the level label in the UI
            self.level_label.config(text="Level: {}".format(self.player.level))
            # Update the UI
            self.root.update()
            # Add a delay to slow down the game loop
            self.root.after(100)
        # Game loop has ended, level 100 reached
        self.root.quit()
class Player:
    def __init__(self):
        self.level = 1
        self.experience = 0
    def level_up(self):
        # Increase the player's level
        self.level += 1
    def gain_experience(self, amount):
        # Increase the player's experience
        self.experience += amount
class Level:
    def __init__(self):
        self.current_level = 1
    def increase_level(self):
        # Increase the current level
        self.current_level += 1
class Quest:
    def __init__(self):
        self.active_quest = None
    def start_quest(self):
        # Start a new quest
        self.active_quest = self.generate_quest()
    def complete_quest(self):
        # Complete the active quest
        self.active_quest = None
    def generate_quest(self):
        # Generate a new quest for the player
        return "New Quest"
    def check_quest_completion(self):
        # Check if the active quest is completed
        return self.active_quest is None
    def reward_player(self):
        # Reward the player upon quest completion
        pass