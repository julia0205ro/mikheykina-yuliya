"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):

    def __init__(self, message):
        self.message = message


class NotEnoughFuel(Exception):

    def __init__(self, message):
        self.message = message


class CargoOverload(Exception):

    def __init__(self, message):
        self.message = message
