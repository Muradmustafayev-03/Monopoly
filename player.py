import math
from cell import Cell
from board import BOARD
from rand import roll_dice


class Player:
    def __init__(self, name: str, position: int = 0, money: int = 1000):
        self.name = name
        self.position = position
        self.money = money
        self.property = []

        self.loans = []

    def __repr__(self):
        return self.name

    def print_stats(self):
        print(
            f'\nPlayer: {self.name}'
            f'\nMoney: {self.money}'
            f'\nProperty: {self.property}'
            f'\nLoans: {sum([loan[1] for loan in self.loans])}'
        )

    def move(self, dice_roll: int):
        self.position = (self.position + dice_roll) % len(BOARD)

    def roll_dice_and_move(self) -> Cell:
        input('Press enter to roll the dice: ')
        old_position = self.position
        dice_roll = roll_dice()
        self.move(dice_roll)

        cell = BOARD[self.position]
        print(f'{self.name} rolled a {dice_roll} and landed on {cell.name}')

        if self.position < old_position:
            print(f'{self.name} passed GO and collected $200')
            self.money += 200

        return cell

    def handle_loans(self):
        loan_repay = sum([loan[1] for loan in self.loans if loan[0] == 1])
        self.loans = [[loan[0] - 1, loan[1]] for loan in self.loans if loan[0] > 1]
        self.money -= loan_repay
        return loan_repay

    def new_loan(self, loan):
        loan = math.ceil(loan / 100) * 100
        if loan > 1000:
            loan = 1000
        self.money += loan
        self.loans.append([10, int(1.1 * loan)])
        return loan

    def take_loan(self):
        if 10 in [pl[0] for pl in self.loans]:
            print('You can take a loan only once at the turn.')
            return
        if len(self.loans) >= 10:
            print('You already have to many loans to repay. The bank declined your request.')
            return
        loan = self.new_loan(int(input('How much money do you want to borrow?\n')))
        print(f'You have borrowed {loan}$. The loan is to be repaid in 10 turns with 10% interest({int(loan * 1.1)}$).')

    def count_collection(self, cell: Cell) -> int:
        return [p.color for p in self.property].count(cell.color)
