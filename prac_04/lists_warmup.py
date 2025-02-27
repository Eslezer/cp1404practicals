"""
CP1404/CP5632 - Practical
Testing lists
"""

# What values do the following expressions have?
# numbers[0] 3
# numbers[-1] 2
# numbers[3] 1
# numbers[:-1] 3, 1, 4, 1, 5, 9
# numbers[3:4] 1
# 5 in numbers = true
# 7 in numbers = false
# "3" in numbers = false
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers = [3, 1, 4, 1, 5, 9, 2]

# change the first element to "ten"
numbers[0] = "ten"

# change the last element to 1
numbers[-1] = 1

# print all elements except the first two
print(numbers[2:])

# check if 9 is an element of numbers and print the result
print(9 in numbers)