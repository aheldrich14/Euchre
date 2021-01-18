import numpy as np
import card
import random

class Deck():
    """
    docstring
    """
    def __init__(self):
        self.cards = []
        self.setupDeck()

    def __str__(self):
        for card in self.cards:
            print(card)
        
        return "End of Deck"

    def setupDeck(self):
        MIN_NUM = 9
        MAX_NUM = 14
        cardVals = [x for x in range(MIN_NUM, MAX_NUM+1)]
        cardSuits = ['C', 'S', 'H', 'D']

        for val in cardVals:
            for suit in cardSuits:
                self.cards.append(card.Card(val, suit))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        card = ''
        if self.cards:
            card = self.cards.pop()
        return card

    
        