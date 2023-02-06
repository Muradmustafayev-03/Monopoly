import random
from board import BOARD


class Player:
    def __init__(self, name: str, position: int = 0, money: int = 1000):
        self.name = name
        self.position = position
        self.money = money
        self.property = []

    @staticmethod
    def roll_dice(num_dices: int = 2) -> int:
        return sum([random.randint(1, 6) for _ in range(num_dices)])

    def move(self, dice_roll: int):
        self.position = (self.position + dice_roll) % len(BOARD)
