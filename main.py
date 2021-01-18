import card
import deck
import player

d = deck.Deck()
pl1 = player.Player(0)
for i in range(0,5):
    pl1.hand.append(d.deal())
print(pl1)
print(d)