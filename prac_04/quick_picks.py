"""
CP1404/CP5632 Practical
Quick pick generator
"""


import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """generate and display quick picks for the user."""
    num_picks = int(input("How many quick picks? "))

    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))


def generate_quick_pick():
    """generate a single quick pick with random numbers"""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    return numbers

main()
