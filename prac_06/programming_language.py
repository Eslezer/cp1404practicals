"""
Estimate: 10 minutes
Actual: Around 10 minutes
"""


class ProgrammingLanguage:
    """represent information about a programming language"""

    def __init__(self, name, typing, reflection, year):
        """initialize a programming language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """true if dynamic"""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """formatted string list of the the programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
