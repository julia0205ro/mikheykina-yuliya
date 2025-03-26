"""
создайте класс `Plane`, наследник `Vehicle`
"""
from hw_2.base import Vehicle
from hw_2.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, cargo: int | float, max_cargo: int | float,
                 weight: int, fuel: int | float, fuel_consumption: int | float,
                 started: bool) -> None:
        super().__init__(weight, fuel, fuel_consumption, started)
        self.max_cargo = max_cargo
        self.cargo = cargo

    def load_cargo(self, new_cargo: int) -> None:
        all_cargo: int | float = new_cargo + self.cargo
        if all_cargo <= self.max_cargo:
            self.cargo = all_cargo
        else:
            message = 'Cargo over load'
            raise CargoOverload(message)

    def remove_all_cargo(self) -> int | float:
        previous_cargo: int | float = self.cargo
        self.cargo = 0
        return previous_cargo
