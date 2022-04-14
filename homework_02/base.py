from abc import ABC
import homework_02.exceptions as exceptions


class Vehicle(ABC):
    weight = 200
    started = False
    fuel = 20
    fuel_consumption = 5

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError()

    def move(self, distance):
        need_fuel = distance * self.fuel_consumption
        if self.fuel >= need_fuel:
            self.fuel -= need_fuel
        else:
            raise exceptions.NotEnoughFuel()
