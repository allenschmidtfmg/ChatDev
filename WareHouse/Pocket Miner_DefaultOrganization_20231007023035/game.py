'''
Pocket Miner - Game File
'''
import tkinter as tk
from player import Player
from environment import Environment
from store import Store
class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.player = Player()
        self.environment = Environment()
        self.store = Store()
        self.create_widgets()
    def create_widgets(self):
        # Create player info display
        self.player_info = tk.Label(self, text="Player Info")
        self.player_info.pack()
        # Create environment display
        self.environment_display = tk.Label(self, text="Environment")
        self.environment_display.pack()
        # Create store button
        self.store_button = tk.Button(self, text="Store", command=self.open_store)
        self.store_button.pack()
    def open_store(self):
        store_window = tk.Toplevel(self)
        store = StoreWindow(store_window, self.store, self.player)
class StoreWindow(tk.Frame):
    def __init__(self, master, store, player):
        super().__init__(master)
        self.store = store
        self.player = player
        self.create_widgets()
    def create_widgets(self):
        # Create store info display
        self.store_info = tk.Label(self, text="Store Info")
        self.store_info.pack()
        # Create purchase buttons for each item
        for item in self.store.items:
            purchase_button = tk.Button(self, text=f"Purchase {item.name} - {item.price} coins", command=lambda item=item: self.purchase_item(item))
            purchase_button.pack()
    def purchase_item(self, item):
        if self.store.purchase_item(item, self.player):
            print(f"Purchased {item.name}")
        else:
            print("Insufficient coins")
class Player:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.coins = 0
class Environment:
    def __init__(self):
        self.name = ""
        self.difficulty = 1
class Store:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def purchase_item(self, item, player):
        if item in self.items:
            if player.coins >= item.price:
                player.coins -= item.price
                item.purchase(player)
                return True
        return False