from abc import ABC, abstractmethod
import random
from Actions import *
from Hand import Hand
from EnumClasses.enums import *


class Player(ABC):
    def __init__(self, name, table):
        self.name = name
        self.table = table
    @abstractmethod
    def action(self):
        pass


class RandomPlayer(Player):

    def __init__(self, name, table):
        super().__init__(name, table)
        self.actions = ['call', 'bet', 'fold', 'check']
        self.hand = None
        self.bet_of_player = 30
        self.money_paid_on_this_round = 0
        self.over_all_money_paid = 0 # כמה כסף שם מתחילת המשחק
        self.still_playing = True
        self.played_this_round = False



    def set_cards(self, cards):
        self.hand = Hand(201, cards)

    def action(self):
        '''  print(self.money_paid_on_this_round)
                print(self.table.money_each_one_need_to_pay_on_this_round)'''
        print(f"{self.name} has {self.hand.money}")
        if not self.table.game_over:
            if self.money_paid_on_this_round == self.table.money_each_one_need_to_pay_on_this_round and self.still_playing and not self.played_this_round:
                action = self.actions[random.randint(1, len(self.actions) - 1)]
                #למה שיעשה פולד אם הוא עדיין יכול לשחק בלי להמר עוד לכן שמתי פה שאם הוא בחר פולד אז יחליף את זה לCHECK
                if action == 'fold':
                    action = 'check'

                print(f"{self.name} does {action}")
                if action == 'bet':
                    self.bet_of_player = random.choice(self.table.possibles_bets)
                    print(f" and raised with {self.bet_of_player}")
                    Bet(self.bet_of_player, self.table, self)
                elif action == 'check':
                    Check(self.table)
                elif action == 'fold':
                    Fold(self.table, self)
            if self.money_paid_on_this_round < self.table.money_each_one_need_to_pay_on_this_round and self.still_playing:
                action = self.actions[random.randint(0, len(self.actions) - 2)]
                # מכיוון שהבחירה רנדומלית בינתיים אנו לא רוצים שמישהו עושה BET זה יגרום לעוד BET ועוד BET לכן ברג שבן אדם אחד עושה BET אז יהיה אפשרות רקלעשות CALL כדי שלא יהיה סתם לולאה מיותרת
                # בהמשך הבוטים יהיו חכמים ועבקבות כך אני אתן להם תאפשרות לעשות BET כחלק מן המשחק
                if action == 'bet':
                    action = 'call'
                #self.table.cardPot
                #action = BotMind.decide(self.hand.cards, self.table.pot, self.table.cardPot)
                print(f"{self.name} does {action}")

                if action == 'call':
                    Call(self.table, self)
                elif action == 'bet':
                    self.bet_of_player = random.choice(self.table.possibles_bets)
                    print(f" and raised with {self.bet_of_player}")
                    Bet(self.bet_of_player, self.table, self)
                elif action == 'fold':
                    Fold(self.table, self)
                self.played_this_round = True

    def new_round(self):
        self.money_paid_on_this_round = 0
        self.played_this_round = False








