try:
    number= float(input(f"insert the number either positive or negative or zero: "))
    if number == 0:
        print(f"The number is equal to zero")
    elif number > 0:
        print(f"The number is positive")
    else:
        print(f"The number is negative")
except ValueError as v:
    print(v, f"--> Please insert a valid number")
