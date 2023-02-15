from cell import Cell
import random

CELL_NAMES = ['Go', 'Mediterranean Ave', 'Community Chest', 'Baltic Ave', 'Income Tax', 'Reading Railroad',
              'Oriental Ave', 'Chance', 'Vermont Ave', 'Connecticut Ave', 'Jail', 'St. Charles Place',
              'Electric Company', 'States Ave', 'Virginia Ave', 'Pennsylvania Railroad', 'St. James Place',
              'Community Chest', 'Tennessee Ave', 'New York Ave', 'Free Parking', 'Kentucky Ave', 'Chance',
              'Indiana Ave', 'Illinois Ave', 'B&O Railroad', 'Atlantic Ave', 'Ventnor Ave', 'Water Works',
              'Marvin Gardens', 'Go to Jail', 'Pacific Ave', 'North Carolina Ave', 'Community Chest',
               'Pennsylvania Ave', 'Short Line', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']

CELL_VALUES = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180, 0, 180, 200, 0,
               220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300, 0, 320, 200, 0, 350, 0, 400]

CELL_RENTS = [[], [2], [], [4], [], [25], [6], [], [6], [8], [], [10], [], [10], [12], [25], [14], [], [14],
              [16], [], [18], [], [18], [20], [25], [22], [22], [], [24], [], [26], [26], [], [28], [], [25],
              [35], [], [50]]

CELL_COLORS = ['Go', 'Brown', 'Community Chest', 'Brown', 'Tax', 'Railroad',
               'Light Blue', 'Chance', 'Light Blue', 'Light Blue', 'Jail', 'Pink',
               'Utility', 'Pink', 'Pink', 'Railroad', 'Orange', 'Community Chest', 'Orange',
               'Orange', 'Red', 'Chance', 'Red', 'Red', 'Railroad', 'Yellow', 'Yellow',
               'Utility', 'Yellow', 'Jail', 'Green', 'Green', 'Community Chest',
               'Green', 'Railroad', 'Dark Blue', 'Chance', 'Dark Blue', 'Tax', 'Dark Blue']


BOARD = [Cell(name=CELL_NAMES[i], value=CELL_VALUES[i], rent=CELL_RENTS[i], color=CELL_COLORS[i])
             for i in range(40)]


def roll_dice(num_dices: int = 2) -> int:
    return sum([random.randint(1, 6) for _ in range(num_dices)])
