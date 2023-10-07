'''
This file contains the Game class which represents the main game logic.
'''
import random
from player import PlayerInfo
class Game:
    def __init__(self):
        self.players = []
    def start(self):
        self.create_players()
        self.play_game()
    def create_players(self):
        num_players = int(input("Enter the number of players: "))
        for i in range(num_players):
            player_name = input(f"Enter the name of player {i+1}: ")
            self.players.append(PlayerInfo(player_name))
    def play_game(self):
        while True:
            for player in self.players:
                player.take_turn()
                if player.is_winner():
                    print(f"{player.name} wins!")
                    return