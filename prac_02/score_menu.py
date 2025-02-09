def get_valid_score():
    """Prompt user for a valid score """
    score = float(input("Enter a valid score from 0-100: "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter a valid score (0-100): "))
    return score


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


def show_stars(score):
    """Print stars equal to the score"""
    print("*" * int(score))


def display_menu():
    """Display the menu options"""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def main():
    """Main function"""
    score = get_valid_score()
    display_menu()
    choice = input("Enter choice: ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Score status: {determine_score_status(score)}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option. Please choose from the menu.")

        display_menu()
        choice = input("Enter choice: ").upper()

    print("Chao")


main()
