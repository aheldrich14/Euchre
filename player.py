import card

class Player():
    """
    docstring
    """
    def __init__(self, pos):
        self.pos = pos
        self.hand = []

    def __str__(self):
        print('Player ' + str(self.pos) + ':')
        
        for card in self.hand:
            print(card)
        
        return "End of Hand"
    
    def selectTrump(self, trumpSuit):
        selectTrump = False
        numTrump = 0
        numOffAce = 0

        for card in self.hand:
            if card.isOffAce(trumpSuit):
                numOffAce += 1
            elif card.isTrump(trumpSuit):
                numTrump += 1
            
            #need at least 3 trumps/off aces to pick trump
            if numTrump+numOffAce >= 3:
                selectTrump = True

        return selectTrump
    
    def screwDealer(self):
        #pick best auit from your hand
        trumpSuit = 'C'
        counter = 0
        for card in self.hand:
            
            if 

        return trumpSuit

    def rankHand(self, trumpSuit):
        handRank = 0
        cardRank = 0
        trumpRank = 10
        bowerRank = 4

        for card in self.hand:
            cardRank = card.value
            if card.isTrump(trumpSuit):
                cardRank += trumpRank
            if card.isBower(trumpSuit):
                cardRank += bowerRank
            handRank += cardRank

        return handRank
