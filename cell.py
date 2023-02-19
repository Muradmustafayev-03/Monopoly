from rand import roll_dice


class Cell:
    def __init__(self, name: str, color: str, value: int, rent: list):
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
            return roll_dice() * 4 if collection < 2 else roll_dice() * 10
        if self.color == 'Railroad':
            return self.__rent * 2 ** (collection - 1)
        if collection == self.__get_collection() and self.level == 0:
            return self.__rent[0] * 2
        return self.__rent[self.level]

    def __get_update_price(self):
        if self.level == 5:
            return None
        if self.color in ['Brown', 'Light Blue']:
            return 50
        if self.color in ['Pink', 'Orange']:
            return 100
        if self.color in ['Red', 'Yellow']:
            return 150
        if self.color in ['Green', 'Dark Blue']:
            return 200
        return None

    def __get_collection(self):
        if self.color in ['Brown', 'Dark Blue']:
            return 2
        if self.color in ['Light Blue', 'Pink', 'Orange', 'Red', 'Yellow', 'Green']:
            return 3
        if self.color == 'Railroad':
            return 4
        if self.color == 'Utility':
            return 2
        return None
