import random
import math

def roll_dice():
    return sum(sorted([random.randint(1, 6) for _ in range(4)])[-3:])

class Character:    
    def __init__(self):
        self.strength = roll_dice()
        self.dexterity = roll_dice()
        self.constitution = roll_dice()
        self.intelligence = roll_dice()
        self.wisdom = roll_dice()
        self.charisma = roll_dice()
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
        return random.choice([
            self.strength, self.dexterity, self.constitution, 
            self.intelligence, self.wisdom, self.charisma
        ])

def modifier(value):
    return math.floor((value - 10) / 2)
