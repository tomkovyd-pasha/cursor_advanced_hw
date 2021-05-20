import House
import Realtor
import Person
import time
import random


if __name__ == '__main__':
    house_instance_0 = House.House(30000, 75)
    house_instance_1 = House.SmallHouse(25000, 35)
    house_instance_2 = House.SmallHouse(27000)
    house_instance_3 = House.SmallHouse(25500)

    person_instance_0 = Person.Person('John', 25, 20000, [house_instance_2])
    realtor_instance = Realtor.Realtor('Ben', 0.15, [house_instance_0, house_instance_1, house_instance_3])

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
                print(f'Person {person_instance_0.name} can buy {str(i)} for {i.cost * (1 - discount)}')
                i.cost *= (1 - discount)
                person_instance_0.buy_house(i)

        time.sleep(3)
