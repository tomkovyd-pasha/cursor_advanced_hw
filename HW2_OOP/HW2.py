from abc import ABC, abstractmethod

# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class


class Animal:
    def eat(self):
        pass

    def sleep(self):
        pass


class Cat(Animal):
    def meow(self):
        pass


class Dog(Animal):
    def bark(self):
        pass


class Wolf(Animal):
    def auf(self):
        pass


class Bird(Animal):
    def tweet(self):
        pass


class Fox(Animal):
    def i_dunno(self):
        pass


class Horse(Animal):
    def hee_haw(self):
        pass


cat_instance, dog_instance, wolf_instance, bird_instance, fox_instance, horse_instance = Cat(), Dog(), Wolf(), Bird(), Fox(), Horse()
animals_tuple = (cat_instance, dog_instance, wolf_instance, bird_instance, fox_instance, horse_instance)
cat_instance.meow()
dog_instance.bark()
wolf_instance.auf()
bird_instance.tweet()
fox_instance.i_dunno()
horse_instance.hee_haw()

for i in animals_tuple:
    print(f'{i} is instance of Animal class - {isinstance(i, Animal)}')


# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
# create an instance of Centaur class and call the common method of these classes and unique.

class Human:
    def eat(self):
        pass

    def sleep(self):
        pass

    def study(self):
        pass

    def work(self):
        pass


class Centaur(Human, Horse):
    def archery(self):
        pass


centaur_instance = Centaur()
centaur_instance.eat()
centaur_instance.archery()

# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
#   a.


class Person:
    def __init__(self):
        self.left_arm = Arm()
        self.right_arm = Arm()


class Arm:
    def __init__(self, fingers=5):
        self.fingers = fingers


#   b.

class Screen:
    def __init__(self, resolution: str):
        self.resolution = resolution


class CellPhone:
    def __init__(self, screen: Screen):
        self.screen = screen


# 3. class Profile:
#     """
#     Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
#     Override a printable string representation of Profile class and return: list of the params mentioned above
#     """


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age, self.sex = name, last_name, phone_number, address, email, birthday, age, sex
        self.param_list = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age, self.sex]

    def __repr__(self):
        return f'Profile{self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age, self.sex}'


profile_instance_0 = Profile('a', 'b', 25, 'add', 'email', '01-01-1990', 24, 1)
print(profile_instance_0)
profile_instance_1 = eval(profile_instance_0.__repr__())
print(profile_instance_1)


# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, screen_resolution, keyboard_keys, touchpad_sensitivity, webcam_mp, ports_count, dynamics_count):
        self.screen_resolution, self.keyboard_keys, self.touchpad_sensitivity, self.webcam_mp, self.ports_count, self.dynamics_count = screen_resolution, keyboard_keys, touchpad_sensitivity, webcam_mp, ports_count, dynamics_count

    def screen(self):
        return f'Screen resolution - {self.screen_resolution}'

    def keyboard(self):
        return f'Keyboard - {self.keyboard_keys}'

    def touchpad(self):
        return f'Touchpad sensitivity - {self.touchpad_sensitivity}'

    def webcam(self):
        return f'Webcam megapixels - {self.webcam_mp}'

    def ports(self):
        return f'Ports count - {self.ports_count}'

    def dynamics(self):
        return f'Dynamics count - {self.dynamics_count}'
