from random import randint


def roll_dices(num_dices: int = 2) -> (int, bool):
    """
    Roll dices and return the sum of the dices and a boolean indicating if the dices are the same.
    :param num_dices: number of dices to roll
    :return: sum of the dices and a boolean indicating if the dices are the same
    """
    dices = [randint(1, 6) for _ in range(num_dices)]
    double = len(set(dices)) == 1
    return sum(dices), double
