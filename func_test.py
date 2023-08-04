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

d = classes.Dealer(10000, [classes.Box(0).receive_cards([deck.pop(0), deck.pop(0)])])
p = classes.Player(1000, b)
while True:
    inp = input()
    if inp == 'rec':
        inp = int(input())
        p.receive_card(deck.pop(0), inp-1)
    
    if inp == 'set':
        inp = int(input())
        summ = int(input())
        p.set_bet(summ, inp-1)
        print(p.money)
    if inp == 'get':
        inp = int(input())
        p.get_bet(inp-1)
        print(p.money)
    if inp == 'sur':
        inp = int(input())
        p.surrender(inp-1)
        print(p.money)
    if inp == 'split':
        inp = int(input())
        print(p.split(inp-1))
        print(p.money)
    if inp == 'double':
        inp = int(input())
        print(p.double(deck.pop(0), inp-1))
        print(p.money)
    if inp == 'ins':
        inp = int(input())
        inp1 = int(input())
        p.insurance(inp1, inp-1)
        print(p.money)
    
    funcs.display(p, d)
