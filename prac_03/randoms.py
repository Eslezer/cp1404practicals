"""
CP1404/CP5632 - Practical
Use of the random built-in module
"""


import random

# Generate random numbers using different random functions
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Answers to the questions:

# What did you see on line 1?
# - Random integers between 5 and 20.
# What was the smallest number you could have seen, what was the largest?
# - The smallest possible number: 5
# - The largest possible number: 20

# What did you see on line 2?
# - A random integer from the sequence 3, 5, 7, 9...
# What was the smallest number you could have seen, what was the largest?
# - The smallest possible number: 3
# - The largest possible number: 9
# Could line 2 have produced a 4?
# - No, because the step is 2, only numbers starting from 3 and then adding 2 can appear.

# What did you see on line 3?
# - A random floating point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# - The smallest possible number: 2.5
# - The largest possible number: 5.5

# Code to produce a random number between 1 and 100 (inclusive)
random_number = random.randint(1, 100)
print(random_number)