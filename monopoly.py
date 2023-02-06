from board import BOARD
from player import Player


class Monopoly:
    @staticmethod
    def play_turn(player: Player):
        input(f'{player.name}, press enter to roll the dice: ')
        dice_roll = player.roll_dice()
        player.move(dice_roll)
        print(f'{player.name} rolled a {dice_roll} and landed on {BOARD[player.position]}')
