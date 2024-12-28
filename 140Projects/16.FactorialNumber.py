from random import randint

number: int = randint(0, 15)
total = 1
for i in range(1, number +1):
    total*=i

print(f"The factorial of {number} is {total}")