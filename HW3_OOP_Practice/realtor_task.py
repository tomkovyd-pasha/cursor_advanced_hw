import random


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, discount, houses):
        self.name = name
        self.houses = houses
        self.discount = discount

    def info(self):
        print(f'Realtor {self.name} can sold this houses ' + ', '.join([str(x) + ' cost(' + str(x.cost) + ')' for x in self.houses]))

    def give_discount(self):
        return self.discount

    def steal_money(self, person):
        if random.randrange(1, 11) == 1:
            person.money *= 0.9
            print(f'Realtor {self.name} steal money. Now {person.name} have {person.money} amount of money')
