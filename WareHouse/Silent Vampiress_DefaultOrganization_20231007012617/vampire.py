'''
This file contains the Vampire class which represents a vampire with different personalities.
'''
import random
class Vampire:
    def __init__(self):
        self.name = "Vampire"
        self.personality = self.generate_personality()
    def generate_personality(self):
        personalities = ["Aggressive", "Calm", "Mysterious", "Elegant"]
        return random.choice(personalities)
    def feed(self):
        # Add feeding logic here
        print("Vampire is feeding...")
    def sleep(self):
        # Add sleeping logic here
        print("Vampire is sleeping...")
    def hunt(self):
        # Add hunting logic here
        print("Vampire is hunting...")
    def transform(self):
        # Add transformation logic here
        print("Vampire is transforming...")
    def drink_blood(self):
        # Add drinking blood logic here
        print("Vampire is drinking blood...")
    def use_powers(self):
        # Add using powers logic here
        print("Vampire is using powers...")