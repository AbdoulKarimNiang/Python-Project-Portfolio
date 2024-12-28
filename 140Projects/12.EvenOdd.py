from random import randint

print("Simple Solution: ")
number: int = randint(0,11)

if number & 1:
    print(f"{number} is Odd!")
else:
    print(f"{number} is even!")


print("Solution with bitwise operation:")

try:
    number: int = int(input(f"insert the number either positive or negative or zero: "))
    if number & 1 == 0:
        print(f"The number is even")
    else:
        print(f"The number is odd")
except ValueError as v:
    print(v, f"--> Please insert a valid number")
