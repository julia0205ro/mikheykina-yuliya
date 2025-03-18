"""
создайте класс `Car`, наследник `Vehicle`
"""
from hw_2.base import Vehicle
from hw_2.engine import Engine


class Car(Vehicle):
    _engine: Engine = None

    def __init__(self, weight: int, fuel: int | float,
                 fuel_consumption: int | float, started: bool, engine: Engine) -> None:
        super().__init__(weight, fuel, fuel_consumption, started)
        self._engine = engine

    @property
    def engine(self) -> Engine:
        return self._engine

    def set_engine(self, engine: Engine) -> None:
        self._engine = engine
