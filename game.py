import classes
import funcs 
import random
import os

deck = funcs.prepare_deck(funcs.make_deck())
#запрос количества боксов:
n = int(input("введите количество боксов, на которых будете играть: "))


#Инициализация PLayer и Dealer
p = classes.Player(10000, [])
d = classes.Dealer(1000000, [classes.Box(0)])

#Проход по боксам, игрок ставит
inp = int(input('ставка на каждый бокс: '))


#Раздача карт на боксы
for i in range(n):
    p.boxes.append(classes.Box(0))
    p.set_bet(inp, i)
    for j in range(2):
        p.receive_card(deck.pop(0), i)


#Раздача карт Диллеру
d.receive_card(deck.pop(0), 0)
d.receive_card(deck.pop(0), 0)
funcs.display(p, d)
#Проход по боксам, взаимодейтсвие игрока с боксами
i = -1
while i < len(p.boxes)-1:
    i += 1
    while True:
        os.system('clear')
        funcs.display(p, d)
        print(f"текущий бокс: {i+1}")
        print(f"ваши деньги: {p.money}")
        inp = input("Действия: receive, double, split, surrender, insurance; stay переключает бокс ")
        if inp == 'stay':
            break

        elif inp == 'receive':
            p.receive_card(deck.pop(0), i)
        
        elif inp == 'double':
            print(p.double(deck.pop(0), i))

        elif inp == 'split':
            print(p.split(i))

        elif inp == 'surrender':
            print(p.surrender(i))

        elif inp == 'insurance':
            print(p.insurance(i))
        os.system('clear')
        funcs.display(p, d)
        print(f"ваши деньги: {p.money}")
        print(f"текущий бокс: {i+1}")
#Диллер открывает вторую карту
#Будет написано с добавлением красивого вывода


#Диллер играет
d.play(deck)


#Проход по боксам, сбор ставок, compare вернет на что умножить ставку
for i in range(len(p.boxes)):
    p.boxes[i].get_win(funcs.compare(p.boxes[i], d.boxes[0]))
    p.get_bet(i)

print(f"ваши деньги: {p.money}")
funcs.display(p, d)
