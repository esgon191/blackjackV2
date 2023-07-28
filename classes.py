import func

class Card:
    def __init__(self, iden):
        self.iden = iden


class Box:
    def __init__(self, bet):
        self.bet = 0
        self.cards = []
        self.points = 0
        self.state = 'def' # def, ins, sur

    def count_points(self, card):
         if card[0] == 'A':
            if self.points <= 21:
                self.points += 11

            else:
                self.points += 1

        elif card[0] in ['J', 'Q', 'K']:
            self.points += 10

        else:
            self.points += int(card[0])        

    def receive_cards(self, cards):
        for card in cards:
            self.cards.append(card)
            self.count_points(card)


    def set_bet(self, bet):
        self.bet = bet
    

    def get_bet(self):
        mid = self.bet
        self.bet = 0
        return mid

class Character:
    def __init__(self, money, boxes):
        self.money = money
        self.boxes = boxes


    def receive_card(self, card, box_id):
        self.boxes[box_id].receive_card(card)



class Player(Character):
    def set_bet(self, bet, box_id): #ставка на бокс с 
        self.boxes[box_id].set_bet(bet)
        self.money -= bet

    def get_bet(self, box_id): #выигрыш (иное получение) ставки идет с бокса, операции со ставкой идут внутри бокса
        self.money += self.boxes[box_id].get_bet()

    def surrender(self, box_id):
        self.money += int(0.5 * self.boxes[box_id].get_set())
        self.boxes[box_id].stat = 'sur'

    def split(self, box_id):
        mid = self.boxes[box_id] #сплитуемый бокс
        self.boxes.append(Box(0))
        for i in range(len(self.boxes)-1, box_id, -1):
            self.boxes[i] = self.boxes[i-1]

        self.boxes[box_id] = Box(int(mid.get_bet() * 0.5).receive_card(mid.cards[0]))
        self.boxes[box_id+1] = self.boxes[box_id]

    def double(self, card, box_id):
        self.receive_card(card, box_id)
        mid = self.boxes[box_id].get_bet()
        self.boxes[box_id].set_bet(2 * mid)


    def insurance(self, bet, box_id):
        self.set_bet(bet, box_id)
        self.boxes[box_id].stat = 'ins'

class Dealer(Character):
    def play(self):
        self.receive_card(card, 0)
    
