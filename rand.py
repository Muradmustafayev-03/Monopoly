import random


def roll_dice(num_dices: int = 2) -> int:
    return sum([random.randint(1, 6) for _ in range(num_dices)])
