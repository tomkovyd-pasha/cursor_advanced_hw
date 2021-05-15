

class Person:
    def __init__(self, name, age, money, houses: list):
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
