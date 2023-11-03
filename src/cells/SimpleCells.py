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
    """

    def __init__(self, name: str = "Go", earn_amount: int = 200):
        super().__init__(0, name)
        self._earn_amount = earn_amount

    @property
    def earn_amount(self):
        return self._earn_amount

    def action(self, player):
        """The player gets money."""
        player.earn(self.earn_amount)


class TaxCell(AbstractCell):
    """
    Class for the Tax cell. This cell takes money from the player.
    """

    def __init__(self, position: int, name: str, tax_amount: int):
        super().__init__(position, name)
        self._tax_amount = tax_amount

    @property
    def tax_amount(self):
        return self._tax_amount

    def action(self, player):
        """The player pays money."""
        player.pay(self.tax_amount)


class GoToJailCell(AbstractCell):
    """
    Class for the Go To Jail cell. This cell sends the player to jail.
    """

    def __init__(self, position: int, name: str):
        super().__init__(position, name)

    def action(self, player):
        """The player goes to jail."""
        player.go_to_jail()
