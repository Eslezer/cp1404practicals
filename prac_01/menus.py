name = input("What's your name?... ")
print('(H)ello\n(G)oodbye\n(Q)uit')
choice = input()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
        print('(H)ello\n(G)oodbye\n(Q)uit')
        choice = input()
    elif choice == "G":
        print(f"Goodbye {name}")
        print('(H)ello\n(G)oodbye\n(Q)uit')
        choice = input()
    else:
        print("Invalid choice")
        print('(H)ello\n(G)oodbye\n(Q)uit')
        choice = input()
print("Finished")