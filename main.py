import card

c = card.Card(11, "C")
c2 = card.Card(11,"S")
c.updateTrump("C")
c2.updateTrump("C")
print((c < c2))
print(c2)