import funcs
import classes

deck = funcs.prepare_deck(funcs.make_deck())

b = classes.Box(10).receive_cards([deck.pop(0), deck.pop(0)])

print(b.get_info())
