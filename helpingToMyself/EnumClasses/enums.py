from enum import Enum


class PotEquity(Enum):
    half = 0.5
    third = 1 / 3
    threeQuarters = 3 / 4
    one_and_half_pot = 1.5


class Round(Enum):
    preFlop = 0
    flop = 1
    turn = 2
    river = 3
