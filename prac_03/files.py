"""
CP1404/CP5632 - Practical
Working with files: writing, reading, and processing data from text files.
"""

# Write user’s name to "name.txt"
name = input("Enter your name: ")
with open("name.txt", "w") as name_file:
    name_file.write(name)

# read name from "name.txt" and print greeting
with open("name.txt", "r") as name_file:
    saved_name = name_file.read().strip()  # newline
print(f"Hi {saved_name}!")

# read first two numbers from numbers.txt and print their sum
with open("numbers.txt", "r") as numbers_file:
    num1 = int(numbers_file.readline())  # read first line
    num2 = int(numbers_file.readline())  # read second line
print(f"Sum of first two numbers: {num1 + num2}")

# read all numbers from numbers.txt and print their total
with open("numbers.txt", "r") as numbers_file:
    total = sum(int(line) for line in numbers_file)
print(f"Total of all numbers: {total}")
