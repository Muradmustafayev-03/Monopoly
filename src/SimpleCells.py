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
