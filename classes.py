import funcs

class Card:
    def __init__(self, iden):
        self.iden = iden


class Box:
    def __init__(self, bet):
        self.bet = bet
        self.cards = []
        self.points = 0
        self.state = 'def' # def, ins, sur, lost, dbl, bj

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
    
    def check_state(self):
        if self.points > 21:
            self.state = 'lost'

        if self.points == 21 and len(self.cards) == 2 and self.state != 'dbl':
            self.state = 'bj' #blackJack
    

    def receive_card(self, card):
        self.cards.append(card)
        self.count_points(card)
        return self
        

    def receive_cards(self, cards):
        for card in cards:
            self.cards.append(card)
            self.count_points(card)
            self.check_state()
        return self

    def set_bet(self, bet):
        self.bet = bet
        return self    

    def get_bet(self):
        mid = self.bet
        self.bet = 0
        return mid
    
    def get_info(self):
        return [self.bet, self.cards, self.points, self.state]

class Character:
    def __init__(self, money, boxes):
        self.money = money
        self.boxes = boxes


    def receive_card(self, card, box_id):
        self.boxes[box_id].receive_card(card)



class Player(Character):
    def set_bet(self, bet, box_id): #ставка на бокс с 
        if self.money >= bet:   
            self.boxes[box_id].set_bet(bet)
            self.money -= bet
            return 'succes'

        else:
            return 'not_enough_money'

    def get_bet(self, box_id): #выигрыш (иное получение) ставки идет с бокса, операции со ставкой идут внутри бокса
        mid = self.boxes[box_id].get_bet()
        self.money += mid
        return mid

    def surrender(self, box_id):
        self.money += int(0.5 * self.get_bet(box_id))
        self.boxes[box_id].state = 'sur'

    def split(self, box_id):
        if len(self.boxes[box_id].cards) == 2 and self.boxes[box_id].cards[0] == self.boxes[box_id].cards[1]:
            mid = self.boxes[box_id] #сплитуемый бокс
            self.boxes.append(Box(0))

            for i in range(len(self.boxes)-1, box_id, -1):
                self.boxes[i] = self.boxes[i-1]

            self.boxes[box_id] = Box(int(mid.bet * 0.5)).receive_card(mid.cards[0])
            self.boxes[box_id+1] = Box(int(mid.bet * 0.5)).receive_card(mid.cards[0])
            return 'succes'

        else:
            return 'wrong_cards'
            

    def double(self, card, box_id):
        mid = self.get_bet(box_id)
        res = self.set_bet(mid * 2, box_id) 
        if res == 'succes':
            self.receive_card(card, box_id)
            self.boxes[box_id].state = 'dbl'
            self.boxes[box_id+1].state = 'dbl'
            return res

        else:
            self.set_bet(mid, box_id)
            return res


    def insurance(self, bet, box_id):
        self.set_bet(bet, box_id)
        self.boxes[box_id].state = 'ins'

class Dealer(Character):
    def play(self):
        self.receive_card(card, 0)
    
