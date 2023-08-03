import random

def make_deck(): #создает колоду
    deck = []
    for i in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        for j in ['H', 'T', 'C', 'S']:
            deck.append([i, j])

    return deck

def prepare_deck(old): #мешает колоду
    new = []
    while len(old) > 0:
        new.append(old.pop(random.randint(0, len(old)-1)))
    return new

def compare(box1, box2): 
    if box1.state == 'lost':
        return 0

    if box2.state == 'bj':
        if box1.state == 'ins':
            return 3

        elif box1.state == 'bj'
            return 1

        else:
            return 0

    elif box2.state == 'lost':
        if box1.state == 'bj':
            return 2.5

        else:
            return 2

    elif box1.state == 'sur':
        return 1 

    else:
        if box2.points > box1.points:
            return 0

        elif box2.points == box1.points:
            return 1

        else:
            return 2


