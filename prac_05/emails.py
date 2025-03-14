"""
CP1404/CP5632 Practical
Email to Name Dictionary
Estimate: 30 minutes
Actual: 20 minutes
"""

def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation != "" and confirmation != "y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()