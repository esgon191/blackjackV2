import classes
import funcs 
import random

deck = funcs.prepare_deck(funcs.make_deck())
"""
n = int(input("kolvo_boxes"))
b = []
for i in range(n):
    b.append(classes.Box(0).receive_cards([deck.pop(0), deck.pop(0)]))

for i in range(n):
    print(b[i].get_info())

p = classes.Player(1000, b)

for i in range(len(p.boxes)):
    p.set_bet(random.randint(1, 50), i)
    print(p.boxes[i].get_info()) """

n = int(input("kolvo boxes "))
b = []
for i in range(n):
    b.append(classes.Box(0).receive_cards([deck.pop(0), deck.pop(0)]))

p = classes.Player(1000, b)
d = classes.Dealer(10000000, [classes.Box(0).receive_cards([deck.pop(0), deck.pop(0)])])


