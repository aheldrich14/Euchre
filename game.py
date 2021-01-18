import deck
import player
import card

class Game():
    """
    docstring
    """
    def __init__(self):
        NUM_PLAYERS = 4
        
        self.players = [player.Player(ix) for ix in range(0,NUM_PLAYERS)]
        self.deck = deck.Deck()
        self.trump = None

        
    def deal(self):
        NUM_CARDS = 5
        for _ in range(0,NUM_CARDS):
            for player in self.players:
                player.hand.append(self.deck.deal())
    
    def startGame(self):
        card = self.deck.deal()
        ROUNDS = 2

        for _ in range(0,ROUNDS):
            if self.trump:  #trump has been declared so don't continue
                break
            for player in self.players: #loop through eah player to see if they select trump
                if player.selectTrump(card):
                    self.trump = card.suit
                    break

        if not self.trump:
            #force dealer to select trump
            pass
        
        self.updateTrump()

    def updateTrump(self):
        for player in self.players: #update new card values for each player
            for card in player.hand:
                card.updateTrump(self.trump)
