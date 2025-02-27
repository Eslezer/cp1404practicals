"""
CP1404/CP5632 Practical
List exercises
"""

# def main():
#     """ask the user for 5 numbers, store them in a list, and display statistics"""
#     numbers = []
#
#     # Collect 5 numbers from the user
#     for i in range(5):
#         number = float(input("Number: "))
#         numbers.append(number)
#
#     # display the information
#     print(f"The first number is {numbers[0]}")
#     print(f"The last number is {numbers[-1]}")
#     print(f"The smallest number is {min(numbers)}")
#     print(f"The largest number is {max(numbers)}")
#     print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")
#
#
# main()


def username_authentication():
    """Check if a username is in the authorised list."""
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
        'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
    ]

    username = input("Enter your username: ")

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

username_authentication()