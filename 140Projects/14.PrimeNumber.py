from random import randint

number = randint(0, 50)

flag = False
if number in [0, 1]:
    print(f"{number} it's not a prime number")
else:
    for single in range(2, number):
        if number % single == 0:
            flag = True
            break
        else:
            pass

    if flag:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")
