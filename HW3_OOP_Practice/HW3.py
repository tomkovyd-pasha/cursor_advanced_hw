from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age, money, is_house_in_property: bool):
        self.start_amount_of_money = money
        self.name = name
        self.age = age
        self.money = money
        self.is_house_in_property = is_house_in_property

    def info(self):
        return f'Name - {self.name}, Age - {self.age}, Money amount - {self.money}, Is house in property - {self.is_house_in_property}'

    def make_money(self):
        self.money += self.start_amount_of_money * 0.1

    def buy_house(self, house):
        if house.cost <= self.money:
            self.money -= house.cost
            self.is_house_in_property = True


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def apply_discount(self, discount):
        self.cost *= 1 - discount


class SmallHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(cost=cost, area=40)


a = SmallHouse(cost=1000)




