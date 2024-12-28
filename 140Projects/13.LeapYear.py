from random import randint

number: int = randint(1900,2020)

if number % 400 == 0:
    print(number)
    print("It's Leap!")
elif number % 100 == 0:
    print(number)
    print("It's not a leap!")
elif number % 4 == 0:
    print(number)
    print("It's Leap!")
else:
    print(number)
    print("It's not a leap!")
