"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """represents cars"""

    def __init__(self, name="", fuel=0):
        """initialise a car

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """drive the car a given distance

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """return a string representation of the car"""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

