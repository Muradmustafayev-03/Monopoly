from player import Player
from monopoly import Monopoly


def main():
    num_players = int(input('Enter number of players: '))
    players = [Player(input(f'Enter the name of the player {i}: ')) for i in range(1, num_players + 1)]
    game = Monopoly(players)
    while True:
        for player in players:
            game.play_turn(player)


if __name__ == '__main__':
    main()
