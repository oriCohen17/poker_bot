class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
    card_ranks = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
        'Q': 12, 'K': 13, 'A': 14
    }

    def valueToNumber(self, card_value):
        return self.card_ranks[card_value]

    def is_stronger(self, card1, card2):
        return self.valueToNumber(card1.value) > self.valueToNumber(card2.value)

    def is_stronger_in_tuple(self,tuple1,tuple2):
        return self.is_stronger(Card(tuple1[0],tuple1[1]),Card(tuple2[0],tuple2[1]))

