# Write a Python program to generate a random number.

from random import randint

lower = 0
upper = 100
random_number = randint(lower, upper)
print(f"Created random number --> {random_number}")
