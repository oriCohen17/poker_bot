from abc import ABC, abstractmethod
from EnumClasses.enums import *


class Action(ABC):
    @abstractmethod
    def __init__(self, player):
        # self.player = player
        pass


class Call(Action):
    def __init__(self, table, player):
        player.hand.remove_money(table.money_each_one_need_to_pay_on_this_round - player.money_paid_on_this_round)
        player.over_all_money_paid += table.money_each_one_need_to_pay_on_this_round - player.money_paid_on_this_round
        table.pot += table.money_each_one_need_to_pay_on_this_round - player.money_paid_on_this_round
        player.money_paid_on_this_round = table.money_each_one_need_to_pay_on_this_round


class Bet(Action):
    def __init__(self, bet, table, player):

        # זה דואג שהוא משלם את מה שהוא חייב בכל מקרה ואז לאחר מכן נותן לו לעשות BET
        # בעקבות כך אם שמת 50 ואז מישהו העלה ב20 ל70 שאתה עושה BET של 20 אז זה כאילו העלית תקופה ל90 כי זה עושה CALL ואז מוסיף את הBET
        if player.money_paid_on_this_round <= table.money_each_one_need_to_pay_on_this_round:
            Call(table, player)
        player.hand.remove_money(bet)  # מסיר את הכסף מהחשבון של השחקן

        table.pot += bet  # מוסיף את הכסף לקופה
        table.money_each_one_need_to_pay_on_this_round += bet  # מגדיר כמה כסף צריך להשים על מנת להמשיך לשחק
        player.money_paid_on_this_round += bet  # מעדכן כמה השחקן שם כסף בסיבוב הזה(פרפלופ, פלופ וכדו...)
        player.over_all_money_paid += bet
        table.last_one_that_bet = player
        #עובר דרך ל השחקנים מהתחלה
        for player_i in table.players:
            if player_i.still_playing and player_i != player:
                player_i.action()


class Check(Action):
    def __init__(self, table):
        pass


class Fold(Action):
    def __init__(self, table, player):
        player.still_playing = False
        table.checks_if_someone_won()
