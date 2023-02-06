class Cell:
    def __init__(self, name: str, value: int, color: str, rent: int):
        self.name = name
        self.value = value
        self.color = color
        self.rent = rent

    def __repr__(self):
        return str(self.value)
