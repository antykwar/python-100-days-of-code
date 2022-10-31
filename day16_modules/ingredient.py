class Ingredient:
    def __init__(self, name: str, amount):
        self.name = name
        self.amount = amount

    def to_dict(self):
        return {self.name: self.amount}
