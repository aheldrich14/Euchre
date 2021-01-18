class Card():
    """
    docstring
    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.trump = False

    def __str__(self):
        suits = {"C":"Clubs", "S":"Spades", "H":"Hearts", "D":"Diamonds"}
        desc = self.getExtValue() + " of " + suits[self.suit]
        return desc

    def __gt__(self, rhsCard):
        isGreaterThan = False

        if self.trump and not(rhsCard.trump):
            isGreaterThan = True #trump always wins
        elif not(self.trump) and not(rhsCard.trump) and (self.value > rhsCard.value):
            isGreaterThan = True
        return isGreaterThan
    
    def getExtValue(self):
        val = self.value
        MAX_NUMERICAL_CARD_VAL = 10
        faces = {11:"J", 12:"Q", 13:"K", 14:"A", 15:"J", 16:"J"}
        if self.value > MAX_NUMERICAL_CARD_VAL:
            val = faces[self.value]
        return str(val)

    def updateTrump(self, trumpSuit):
        LEFT_BOWER_VAL = 16
        RIGHT_BOWER_VAL = 15
        if self.isTrump(trumpSuit):
            self.trump = True
            if self.isBower(trumpSuit):
                self.value = LEFT_BOWER_VAL
        elif self.isBower(trumpSuit):
            self.trump = True
            self.suit = trumpSuit
            self.value = RIGHT_BOWER_VAL

    def isTrump(self, trumpSuit):
        isTrump = False
        if self.suit == trumpSuit:
            isTrump = True
        return isTrump

    def isBower(self, trumpSuit):
        isBower = False
        suitColors = {"C":"S", "S":"C", "H":"D", "D":"H"}
        if self.isJack() and ( (suitColors[self.suit] == trumpSuit) or (self.suit == trumpSuit) ):
            isBower = True
        return isBower

    def isOffAce(self, suit):
        isAce = False
        ACE_VAL = 14
        if self.value == ACE_VAL and self.suit != suit:
            isAce = True
        return isAce

    def isJack(self):
        isJack = False
        JACK = 11
        if self.value == JACK:
            isJack = True
        return isJack
