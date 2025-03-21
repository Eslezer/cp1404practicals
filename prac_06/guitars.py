"""
Estimate: 10 minutes
Actual: 7 minutes
"""

from guitar import Guitar


def main():
    """storing the guitars"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "": #if the name is field left empty, the program finishes
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    # previous sample guitars, uncomment for quick testing
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):  # enumerates the guitars to make it callable (iterable?)
        vintage_string = " (vintage)" if guitar.is_vintage() else ""   # if vintage add a little note saying (vintage)
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
