from abc import ABC, abstractmethod


class AbstractCell(ABC):
    """
    Abstract class for all monopoly cells.

    Attributes:
        position (int): The position of the cell on the board. From 0 to len(board)-1.
        name (str): The name of the cell.

    Methods:
        action: Abstract method for the action of the cell.
    """

    def __init__(self, position: int, name: str):
        self._position = position
        self._name = name

    @property
    def position(self):
        return self._position

    @property
    def name(self):
        return self._name

    @abstractmethod
    def action(self, *args, **kwargs):
        """Abstract method for the action of the cell."""
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
