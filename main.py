import random


class Cell:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Player:
    def __init__(self, name, position=0):
        self.name = name
        self.position = position

    @staticmethod
    def roll_dice(num_dices=2):
        return sum([random.randint(1, 6) for _ in range(num_dices)])

    def move(self, dice_roll):
        self.position = (self.position + dice_roll) % len(Monopoly.board)


class Monopoly:
    board = [Cell(value) for value in range(0, 400, 10)]

    @staticmethod
    def play_turn(player):
        input(f'{player.name}, press enter to roll the dice: ')
        dice_roll = player.roll_dice()
        player.move(dice_roll)
        print(f'{player.name} rolled a {dice_roll} and landed on {Monopoly.board[player.position]}')


if __name__ == '__main__':
    num_players = int(input('Enter number of players: '))
    players = [Player(input(f'Enter the name of the player {i}: ')) for i in range(1, num_players + 1)]
    game = Monopoly()
    while True:
        for player in players:
            game.play_turn(player)
