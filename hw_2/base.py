from abc import ABC

from hw_2.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int = 0
    _started: bool = False
    fuel: int | float = 0
    fuel_consumption: int | float = 0

    def __init__(self, weight: int, fuel: int | float,
                 fuel_consumption: int | float, _started: bool) -> None:
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    @property
    def started(self) -> bool:
        return self._started

    @started.setter
    def started(self, value: bool):
        self._started = value

    def start(self):
        if self._started:
            raise ValueError('Already started')
        else:
            if self.fuel > 0:
                self._started = True
            else:
                message = 'Insufficient fuel'
                raise LowFuelError(message)

    def move(self, distance) -> None:
        if not self._started:
            raise ValueError('Not started')
        else:
            needed_fuel: float = self.fuel_consumption * distance / 100
            if self.fuel >= needed_fuel:
                self.fuel: int | float = self.fuel - needed_fuel
            else:
                message = 'Not enough fuel'
                raise NotEnoughFuel(message)
