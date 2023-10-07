'''
Pocket Miner - Store File
This file contains the Store class for Pocket Miner.
'''
class Store:
    def __init__(self):
        self.items = []
        self.prices = {}
    def add_item(self, item, price):
        self.items.append(item)
        self.prices[item] = price
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            del self.prices[item]
    def buy_item(self, item):
        if item in self.items:
            price = self.prices[item]
            # Perform the purchase logic here
            print(f"Buying {item} for {price} coins.")
        else:
            print(f"{item} is not available in the store.")
    def sell_item(self, item):
        if item in self.items:
            price = self.prices[item]
            # Perform the selling logic here
            print(f"Selling {item} for {price} coins.")
        else:
            print(f"{item} is not available in the store.")