"""
Estimate: 6 minutes
Actual: 5 minutes
"""


class Guitar:
    """class for a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self, current_year=2024):
        """get the age of the guitar"""
        return current_year - self.year

    def is_vintage(self):
        """return true if guitar is 50 years old or older"""
        return self.get_age() >= 50

    def __str__(self):
        """return a nicely formatted string representation of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"


    def __lt__(self, other):
        """compare guitars by their year"""
        return self.year < other.year