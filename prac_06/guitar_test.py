"""
Estimate: 5 minutes
Actual: 4 minutes
"""

from guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500)

    print(f"{guitar1.name} get_age() expected 102. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() expected 11. Got {guitar2.get_age()}")

    print(f"{guitar1.name} is_vintage() expected true. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() expected false. Got {guitar2.is_vintage()}")


main()
