import dataclasses
from abc import ABC, abstractmethod

VEHICLE_ALLOWED_TYPES = ('bike', 'car', 'bus', 'truck')

WASH_LEVEL = {
    'Express': 0,
    'Inside': 1,
    'Outside': 2,
    'Complex': 3,
    'Full': 4,
    'Super': 5,
    'Shiny': 6
}
MAX_WASH_LVL = max(WASH_LEVEL.values())


class CarWashLux(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PepperWash(metaclass=CarWashLux):
    def __init__(self, workers, bikes=None, cars=None, buses=None, trucks=None):
        self.bikes, self.cars, self.buses, self.trucks, self.workers = bikes, cars, buses, trucks, workers

    @staticmethod
    def info():
        print(f'types - bikes, cars, buses, trucks, workers')

    def employee_info(self):
        print(f'now we have {len(self.workers)} workers')

    def daily_summary(self):
        vehicles_count = [x for x in [self.bikes, self.cars, self.buses, self.trucks] if x is not None]
        print(f'today we have such vehicles - {len(vehicles_count)}')


class VehicleMeta(ABC):
    def __init__(self, wash_type, vehicle_type, additional_service):
        self.wash_type, self._vehicle_type, self.additional_service = wash_type, vehicle_type, additional_service

    # @abstractmethod
    # def vehicle_type(self):
    #     raise NotImplementedError
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        if vehicle_type in VEHICLE_ALLOWED_TYPES:
            self._vehicle_type = vehicle_type
            print(f'Your vehicle type is {self._vehicle_type}')
        else:
            raise Exception(f'Wrong vehicle type. Not able to set {vehicle_type}')

    @abstractmethod
    def dirty_level(self):
        raise NotImplementedError

    @abstractmethod
    def is_clean(self):
        raise NotImplementedError


class Vehicle(VehicleMeta):
    def __init__(self, wash_type, vehicle_type, additional_service):
        self.clean_lvl = 0
        super().__init__(wash_type, vehicle_type, additional_service)

    def dirty_level(self):
        return WASH_LEVEL[self.wash_type]

    def clean(self):
        if self.dirty_level() > self.clean_lvl:
            print('Now worker cleans vehicle')
            print(f'Wash level before cleaning - {self.clean_lvl}')
            self.clean_lvl += 1
            print(f'Wash level after cleaning - {self.clean_lvl}')

    def is_clean(self):
        return self.clean_lvl == self.dirty_level()


class WorkerMeta(ABC):
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    @abstractmethod
    def check_dirty_level(self):
        raise NotImplementedError

    @abstractmethod
    def wash(self):
        raise NotImplementedError

    @abstractmethod
    def polish(self):
        raise NotImplementedError


class Worker(WorkerMeta):
    def __init__(self, name, vehicle):
        super().__init__(name, vehicle)

    def check_dirty_level(self):
        return f'Vehicle dirty level = {self.vehicle.dirty_level()}'

    def wash(self):
        while not self.vehicle.is_clean():
            self.vehicle.clean()
        print('Vehicle clean')
        self.polish() if self.vehicle.additional_service else None

    def polish(self):
        print('Vehicle polished')


# wash_type, vehicle_type, additional_service
# bikes, cars, buses, trucks, workers

bike_instance_0 = Vehicle('Outside', 'bike', True)
worker_instance_0 = Worker('John', bike_instance_0)
car_wash_instance = PepperWash(workers=[worker_instance_0], bikes=[bike_instance_0])

car_wash_instance.info()
car_wash_instance.daily_summary()
car_wash_instance.employee_info()

worker_instance_0.check_dirty_level()
worker_instance_0.wash()

