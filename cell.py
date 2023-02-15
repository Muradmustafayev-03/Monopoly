from board import CELL_COLORS, roll_dice


class Cell:
    def __init__(self, name: str, color: str, value: int, rent: int):
        self.name = name
        self.color = color
        self.value = value
        self.__rent = rent
        self.owner = None
        self.level = 0

    def __repr__(self):
        return self.name

    def get_rent(self, collection: int = 1) -> int:
        if self.color == 'Utility':
            return roll_dice() * 4 if collection == 1 else roll_dice() * 10
        if self.color == 'Railroad':
            return self.__rent * 2 ** (collection - 1)
        if collection == CELL_COLORS.count(self.color):
            return self.__rent * 2
        return self.__rent
