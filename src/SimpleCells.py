from AbstractCell import AbstractCell


class PassiveCell(AbstractCell):
    """
    Class for all passive monopoly cells. These cells do not have any action.
    Examples: Free Parking, Jail (just visiting)
    """

    def __init__(self, position: int, name: str):
        super().__init__(position, name)

    def action(self, *args, **kwargs):
        """Passive cells do not have any action."""
        pass


class GoCell(AbstractCell):
    """
    Class for the Go cell. This cell gives money to the player.

    Attributes:
        name (str): The name of the cell.
        earn_amount (int): The amount of money the player gets when he passes from this cell.
    """

    def __init__(self, name: str = "Go", earn_amount: int = 200):
        super().__init__(0, name)
        self._earn_amount = earn_amount

    @property
    def earn_amount(self):
        return self._earn_amount

    def action(self, player):
        """The player gets money."""
        player.add_money(self.earn_amount)
