import random
from abc import ABC, abstractmethod

class Deck:

    def __init__(self):
        """יוצר חפיסה סטנדרטית של 52 קלפים"""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [f"{rank} of {suit}" for suit in suits for rank in ranks]


    def shuffle(self):
        """מערבבת את הקלפים"""
        #print(self.cards)
        random.shuffle(self.cards)

    def draw_card(self):
        """שולפת קלף בודד מהחפיסה"""
        if self.cards:
            return self.cards.pop()
        else:
            return "No cards left in the deck"