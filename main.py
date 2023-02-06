import random


class Monopoly:
    def __init__(self, num_players):
        self.board = [0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0, 80, 0, 90, 0, 100]
        self.players = [{"position": 0, "name": f"Player {i}"} for i in range(1, num_players + 1)]

    def play_turn(self, player):
        input(f"{player['name']}, press enter to roll the dice: ")
        dice_roll = random.randint(1, 6) + random.randint(1, 6)
        player["position"] = (player["position"] + dice_roll) % len(self.board)
        print(f"{player['name']} rolled a {dice_roll} and landed on {self.board[player['position']]}")


game = Monopoly(int(input("Enter number of players: ")))
while True:
    for player in game.players:
        game.play_turn(player)
