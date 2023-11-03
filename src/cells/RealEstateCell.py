from abc import ABC, abstractmethod
from AbstractCell import AbstractCell
from ..utils.random_utils import roll_dices


class RealEstateCell(ABC, AbstractCell):
    """
    Abstract class for different kinds of real estate cells. Can be bought and sold,
    therefore has price and owner.
    """

    def __init__(self, position: int, name: str, price: int):
        super().__init__(position, name)
        self._price = price
        self._owner = None

    @property
    def price(self):
        return self._price

    @property
    def owner(self):
        return self._owner

    @property
    @abstractmethod
    def rent_amount(self):
        """Abstract method to calculate rent amount. Should be implemented according to the type of property."""
        return

    @price.setter
    def price(self, value: int):
        self._price = value

    @owner.setter
    def owner(self, player):
        self._owner = player

    def action(self, player):
        if self.owner is None:
            # buy or auction
            pass  # to implement later
        else:
            self.collect_rent(player)

    def buy_from_bank(self, player):
        assert self.owner is None, 'This property is owned by a player.'
        player.pay(self.price)
        player.properry.add(self)

    def sell_to(self, player, price):
        assert self.owner is not None, 'This property belongs to the bank.'

        self.owner.property.remove(self)
        self.owner.earn(price)

        player.properry.add(self)
        player.pay(price)

    def collect_rent(self, player):
        assert self.owner is not None, 'This property belongs to the bank.'
        player.pay(self.rent_amount)

    def count_collection(self) -> int:
        assert self.owner is not None, 'This property belongs to the bank.'
        count = 0
        for real_estate in self.owner.property:
            if type(real_estate) == type(self):
                count += 1
        return count

    def count_total(self, board):
        count = 0
        for cell in board:
            if type(cell) == type(self):
                count += 1
        return count


class RailwayCell(RealEstateCell):
    """
    Class for the Railway cell. This cell can be bought and sold.
    """

    def __init__(self, position: int, name: str):
        super().__init__(position, name, 200)

    @property
    def rent_amount(self):
        return 25 * (2 ** (self.count_collection() - 1))


class UtilityCell(RealEstateCell):
    """
    Class for the Utility cell. This cell can be bought and sold.
    """

    def __init__(self, position: int, name: str):
        super().__init__(position, name, 150)

    @property
    def rent_amount(self):
        multiplier = 10 if self.count_collection() == self.count_total() else 4
        return roll_dices() * multiplier


class StreetCell(RealEstateCell):
    """
    Class for the Street cell. This cell can be bought and sold.
    """

    def __init__(self, position: int, name: str, price: int, color: str, rents: tuple):
        super().__init__(position, name, price)
        self._color = color
        self._rents = rents
        self._houses = 0
        self._hotel = False

    @property
    def color(self):
        return self._color

    @property
    def rent_amount(self):
        if self.hotel:
            return self.rents[-1]
        elif self.houses == 0 and self.count_collection() == self.count_total():
            return self.rents[0] * 2
        else:
            return self.rents[self.houses]

    def count_collection(self):
        count = 0
        for real_estate in self.owner.property:
            if type(real_estate) == type(self):
                if real_estate.color == self.color:
                    count += 1
        return count

    def build_house(self):
        pass  # to implement later

    def build_hotel(self):
        pass  # to implement later
