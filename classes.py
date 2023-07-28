class Character:
    def __init__(self, money, cards):
        self.money = money
        self.cards = cards
        self.points = 0
        slef.count_points(cards)

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

    def receive_card(self, card):
        self.cards.append(card)
        self.countpoints(card)

class Dealer(Character):
    def turn(self):
        if self.points <= 16:
            self.receive_card()


class Player(Character):
    def bet(self, bet):
        self.bet = bet
