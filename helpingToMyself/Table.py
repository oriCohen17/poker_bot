from Deck import Deck
from abc import ABC, abstractmethod
from EnumClasses.enums import *
from Players import *

class Table:
    def __init__(self):
        self.deck = Deck() #מכין חבילת קלפים
        self.deck.shuffle() # מערבב אותה
        self.pot = 0 # סכום בקופה
        self.money_each_one_need_to_pay_on_this_round = 0
        self.round = Round.preFlop
        self.cardPot = [] #הקלפים שעל השולחן
        self.players = []
        self.game_over = False
        self.game_functions = [self.PreFlop, self.Flop, self.Turn, self.River]
        self.possibles_bets = [self.pot*PotEquity.half.value, self.pot*PotEquity.third.value, self.pot*PotEquity.threeQuarters.value,
                               self.pot*PotEquity.one_and_half_pot.value]
        self.last_one_that_bet = None


    def start_game(self):
        self.deal_cards()

        for player in self.players:
            print(f"{player.name} has {player.hand.cards_in_string()} cards")

        print("")
        for func in self.game_functions:
            if not self.game_over:
                func()
            else:
                break






    def PreFlop(self):
        self.money_each_one_need_to_pay_on_this_round = 0
        for player in self.players:
            player.hand.remove_money(1)
            self.pot += 1
        self.possibles_bets = [self.pot*PotEquity.half.value, self.pot*PotEquity.third.value, self.pot*PotEquity.threeQuarters.value,
                               self.pot*PotEquity.one_and_half_pot.value]
        if self.round == Round.preFlop:
            self.going_through_players()
            while not self.is_every_one_who_plays_paid():
                self.going_through_players()
            self.round = Round.flop

    def going_through_players(self):
        for player in self.players:
            player.action()
        self.players = [player for player in self.players if player.still_playing]
        for player in self.players:
            player.new_round()


    def Flop(self):
        self.money_each_one_need_to_pay_on_this_round = 0
        if self.round == Round.flop:
            self.draw_flop()
            self.going_through_players()
            while not self.is_every_one_who_plays_paid():
                self.going_through_players()
            self.round = Round.turn
    def Turn(self):
        self.money_each_one_need_to_pay_on_this_round = 0
        if self.round == Round.turn:
            self.draw_turn_or_river()
            self.going_through_players()
            while not self.is_every_one_who_plays_paid():
                self.going_through_players()
            self.round = Round.river

    def River(self):
        self.money_each_one_need_to_pay_on_this_round = 0
        if self.round == Round.river:
            self.draw_turn_or_river()
            self.going_through_players()
            while not self.is_every_one_who_plays_paid():
                self.going_through_players()


    def add_player(self, name):
        self.players.append(RandomPlayer(name, self))



    def deal_cards(self):
        for player in self.players:
            player.set_cards([self.deck.draw_card(), self.deck.draw_card()])

    def draw_flop(self):
        self.deck.draw_card() #שעיר לעזעזל
        for i in range(3):
            self.cardPot.append(self.deck.draw_card())

        print(self.cardPot)

    def draw_turn_or_river(self):
        self.deck.draw_card()
        self.cardPot.append(self.deck.draw_card())

        print(self.cardPot)

    def checks_if_someone_won(self):
        players_in_game = [player for player in self.players if player.still_playing]
        if len(players_in_game) == 1:
            print(players_in_game[0].name + " WON!")
            self.game_over = True
            self.deal_money(players_in_game)

        # צריך גם לבדוק את הקלפים של השחקן ביחס לקלפים בשולחן

    def deal_money(self, players_in_game):
        for player in players_in_game:
            if len(players_in_game) == 1:
                player.hand.add_money(self.pot)
                print(f"the pot: {self.pot}")
                print(f"{player.name} has {player.hand.money}")



    def add_to_pot(self, value):
        self.pot += value

    def is_every_one_who_plays_paid(self):
        for player in self.players:
            if player.still_playing:
                if player.money_paid_on_this_round <= self.money_each_one_need_to_pay_on_this_round:
                    return True
                else:
                    return False
                    # אמור להציע להם רק CALL ,BET או FOLD





