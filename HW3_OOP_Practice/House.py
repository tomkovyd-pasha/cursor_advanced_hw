

class House:
    def __init__(self, cost, area):
        self.area = area
        self.cost = cost

    def apply_discount(self, discount):
        self.cost *= 1 - discount

    def __str__(self):
        return f'HouseId{id(self)}'

    def __repr__(self):
        return f'HouseId{id(self)}'


class SmallHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(cost, area)
