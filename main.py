import random


class Monopoly:
    def __init__(self):
        self.board = list(range(40))
        self.player_position = 0

    def play_turn(self):
        input("Press enter to roll the dice: ")
        dice_roll = random.randint(1, 6) + random.randint(1, 6)
        self.player_position = (self.player_position + dice_roll) % len(self.board)
        print("You rolled a", dice_roll, "and landed on", self.board[self.player_position])


game = Monopoly()
while True:
    game.play_turn()
