from board import BOARD
from cell import Cell
from player import Player


class Monopoly:
    @staticmethod
    def check_funds(player: Player, cost: int) -> bool:
        return player.money >= cost

    @staticmethod
    def collect_rent(player: Player, cell: Cell):
        if cell.owner is None:
            return
        if cell.owner == player:
            return
        player.money -= cell.rent
        cell.owner.money += cell.rent
        print(f'{player.name} paid {cell.rent} to {cell.owner.name}')

    @staticmethod
    def buy_property(player: Player, cell: Cell):
        if cell.value == 0:
            return
        if player.money < cell.value:
            print(f"{player.name}, you don't have enough money to buy {cell.name} for {cell.value}")
            return
        if cell.owner is not None:
            return
        choice = input(f'Do you want to buy {cell.name} for {cell.value}? (y/n): ')
        if choice.lower() == 'y':
            player.money -= cell.value
            player.property.append(cell)
            cell.owner = player
            print(f'{player.name} bought {cell.name}')
        else:
            print(f'{player.name} decided not to buy {cell.name}')

    def play_turn(self, player: Player):
        print(f'\n{player.name}\nMoney: {player.money}\nProperty: {player.property}')
        input('Press enter to roll the dice: ')
        dice_roll = player.roll_dice()
        player.move(dice_roll)
        cell = BOARD[player.position]
        print(f'{player.name} rolled a {dice_roll} and landed on {cell.name}')

        self.collect_rent(player, cell)
        self.buy_property(player, cell)
