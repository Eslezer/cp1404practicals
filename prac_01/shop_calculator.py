items = int(input("How many items do you wish to buy?... "))
while items < 0:
    items = int(input("Invalid number of items, re enter... "))
shopping_list = []

for i in range(1, items + 1):
    itemprice = int(input(f"What's the price of item {i}?... $"))
    shopping_list.append(itemprice)

print(f"The number of items is {items}")
for i in shopping_list:
    print(f"Item price: ${i}")

stotal = sum(shopping_list)

if stotal > 100:
    total = stotal * 0.9
    print(f"Total: ${total:.2f}")
else:
    print(f"Total: ${stotal:.2f}")