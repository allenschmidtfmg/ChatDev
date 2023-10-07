'''
Pocket Miner - Store File
'''
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def purchase(self, player):
        # Handle item purchase logic
        pass
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