"""
CP1404/CP5632 Practical
Guitar program to store and read guitar's details
"""


import csv
from guitar import Guitar

FILENAME = "guitars.csv"

def load_guitars(filename):
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def add_user_guitars(guitars):
    print("\nAdd your own guitars (leave name empty to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))

def main():
    guitars = load_guitars(FILENAME)
    print("Original list of guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)

    add_user_guitars(guitars)
    save_guitars(FILENAME, guitars)
    print("\nUpdated guitars have been saved.")

if __name__ == "__main__":
    main()
