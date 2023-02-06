from board import BOARD
from player import Player


class Monopoly:
    @staticmethod
    def check_funds(player: Player, cost: int) -> bool:
        return player.money >= cost

    @staticmethod
    def play_turn(player: Player):
        print(f'\n{player.name}\nMoney: {player.money}\nProperty: {player.property}')
        input('Press enter to roll the dice: ')
        dice_roll = player.roll_dice()
        player.move(dice_roll)
        cell = BOARD[player.position]
        print(f'{player.name} rolled a {dice_roll} and landed on {cell.name}')

        if cell.value == 0 or cell.owner:
            return
        if player.money < cell.value:
            print(f"{player.name}, you don't have enough money to buy {cell.name} for {cell.value}")
            return
        choice = input(f'Do you want to buy {cell.name} for {cell.value}? (y/n): ')
        if choice.lower() == 'y':
            player.money -= cell.value
            player.property.append(cell)
            cell.owner = player
            print(f'{player.name} bought {cell.name}')
        else:
            print(f'{player.name} decided not to buy {cell.name}')



