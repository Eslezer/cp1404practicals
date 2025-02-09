"""
CP1404/CP5632 - Practical
Refactored score.py
"""
import random


def determine_score_status(score):
    """Determine the status of the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 89:
        return "Excellent"
    elif score > 49:
        return "Passable"
    else:
        return "Bad"


def main():
    """Main function to enter score and determine the status"""
    score = float(input("Enter score: "))
    print(determine_score_status(score))

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}, Status: {determine_score_status(random_score)}")


main()
