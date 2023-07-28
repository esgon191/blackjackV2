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

