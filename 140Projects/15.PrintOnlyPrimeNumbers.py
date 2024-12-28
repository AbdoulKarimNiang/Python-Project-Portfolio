numbers = [number for number in range(0, 22)]
flag = False
for number in numbers:
    if number in [0, 1]:
        pass
    else:
        for single in range(2, number):
            flag = False
            if number % single == 0:
                flag = True
                break
            else:
                pass
        if not flag:
            print(f"{number} is a prime number")
