class Hand:
    def __init__(self, money, cards):
        self.money = money
        self.cards = cards
    def remove_money(self, amount):
        self.money -= amount

    def add_money(self, amount):
        self.money += amount

    def cards_in_string(self):
        return f"{self.cards[0]} and {self.cards[1]}"

