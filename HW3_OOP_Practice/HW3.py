from abc import ABC, abstractmethod
import random
import time


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Person:
    def __init__(self, name, age, money, houses=[]):
        self.start_amount_of_money = money
        self.name = name
        self.age = age
        self.money = money
        self.houses = houses

    def info(self):
        print(f'Person - Name - {self.name}, Age - {self.age}, Money amount - {self.money}, houses in property - {len(self.houses)}')

    def make_money(self):
        self.money += self.start_amount_of_money * 0.025
        print(f'Person {self.name} received money, now {self.name} have {self.money} amount of money')

    def buy_house(self, house):
        if house.cost <= self.money:
            self.money -= house.cost
            self.houses.append(house)
            print(f'{self.name} buy house {str(house)}')


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


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, discount, houses=[]):
        self.name = name
        self.houses = houses
        self.discount = discount

    def info(self):
        print(f'Realtor {self.name} can sold this houses ' + ', '.join([str(x) for x in self.houses]))

    def give_discount(self):
        return self.discount

    def steal_money(self, person):
        if random.randrange(1, 11) == 1:
            person.money *= 0.9
            print(f'Realtor {self.name} steal money. Now {person.name} have {person.money} amount of money')


if __name__ == '__main__':
    house_instance_0 = House(30000, 75)
    house_instance_1 = SmallHouse(25000, 35)
    house_instance_2 = SmallHouse(27000)
    house_instance_3 = SmallHouse(25500)

    person_instance_0 = Person('John', 25, 20000, [house_instance_2])
    realtor_instance = Realtor('Ben', 0.15, [house_instance_0, house_instance_1, house_instance_3])

    current_count_of_houses_in_property = len(person_instance_0.houses)
    while len(person_instance_0.houses) < current_count_of_houses_in_property + 1:
        person_instance_0.info()
        realtor_instance.info()
        person_instance_0.make_money()
        realtor_instance.steal_money(person_instance_0)

        discount = 0
        if random.randrange(1, 11) == 1:
            discount = realtor_instance.give_discount()
            print(f'Realtor {realtor_instance.name} give discount - {discount}')

        for i in realtor_instance.houses:
            if person_instance_0.money >= i.cost * (1 - discount):
                print(f'Person {person_instance_0.name} can buy {str(i)} for {i.cost * (1- discount)}')
                i.cost *= (1 - discount)
                person_instance_0.buy_house(i)

        time.sleep(3)
