base = None
height = None

def ask_numeric(value, name:str):
    while not isinstance(value, (int,float)):
        try:
            value = float(input(f"Please insert the {name} of your triangle: "))
        except ValueError as e:
            print(e)
            print(f"Please insert proper numbers either int or float")    
    return value

base = ask_numeric(base, "base")
height = ask_numeric(height, "height")

area = base * height / 2
print(f"The triangle area with base {base} and height {height} is {area}")
