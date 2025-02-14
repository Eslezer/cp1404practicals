"""
CP1404/CP5632 - Practical
password_stars.py

length checker and print the length of stars
"""
min_length = 10


def main():
    """User enters password"""
    password = input("Enter password: ")
    pass_length = len(password)
    do_check(pass_length)


def do_check(pass_length):
    """Length is checked to be 10 characters or more"""
    if pass_length > min_length:
        print("correct")
        for i in range(pass_length):
            print("*", end="")
    else:
        print("\ninvalid length")
        main()



main()

