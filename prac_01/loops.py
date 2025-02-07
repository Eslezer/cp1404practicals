for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

star = int(input("How many stars do you want to print?... "))
for i in range(0, star):
    print("*", end='')
print()

stars = int(input("How many stars do you want to print?... "))
for i in range(1, stars + 1):
    for j in range(1, i + 1):
        print("* ", end="")
    print("")
print()