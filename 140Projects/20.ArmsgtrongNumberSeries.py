def ask_numeric(value, name:str):
    while not isinstance(value, (int,float)):
        try:
            value = int(input(f"Please insert the {name} value: "))
        except ValueError as e:
            print(e)
            print(f"Please insert proper numbers either int or float")    
    return value

if __name__ == '__main__':

    lower = None
    upper = None
    lower: str = ask_numeric(lower, 'lower')
    upper: str = ask_numeric(upper, 'upper')

    for i in range(lower, upper+1):
        total = 0
        string_number = str(i)
        number_digits = len(string_number)
        for digit in string_number:
            value = int(digit) ** number_digits
            total += value

        if total == int(i):
            print(f"{i} it's an Amstrong number!")
        else:
            print(f"{i} it's not an Amstrong number!")

