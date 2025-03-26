from abc import ABC

from hw_2.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight: int = 0, fuel: int | float = 0,
                 fuel_consumption: int | float = 0, started: bool = False) -> None:
        self._weight = weight
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption
        self._started = started

    @property
    def started(self) -> bool:
        return self._started

    @started.setter
    def started(self, value: bool):
        self._started = value

    @property
    def weight(self) -> int:
        return self._weight

    @weight.setter
    def weight(self, value: int):
        self._weight = value

    @property
    def fuel(self) -> int | float:
        return self._fuel

    @fuel.setter
    def fuel(self, value: int | float):
        self._fuel = value

    @property
    def fuel_consumption(self) -> int | float:
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value: int | float):
        self._fuel_consumption = value

    def start(self):
        if self._started:
            raise ValueError('Already started')
        else:
            if self.fuel > 0:
                self.started = True
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
