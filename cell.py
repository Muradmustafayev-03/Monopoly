class Cell:
    def __init__(self, name: str, color: str, value: int, rent: int):
        self.name = name
        self.color = color
        self.value = value
        self.rent = rent
        self.owner = None

    def __repr__(self):
        return self.name
