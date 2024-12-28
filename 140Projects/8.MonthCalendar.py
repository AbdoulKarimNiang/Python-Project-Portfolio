from calendar import month

year = None
month_number = None

def get_value(value, name:str, digits: int) -> int:
    while not isinstance(value, (int, float)) :
    
        try:
            if name == "month":
                value: int = int(input(f"Please insert the {name} with up to {digits} digits: "))
            elif name == "year":
                value: int = int(input(f"Please insert the {name} in {digits} digits: "))
            else:
                continue
        except ValueError as v:
            print(v, "Please insert a valid numeric value")
            print(f"The value must have exactly {digits} digits.")
        
    return value

year: int = get_value(year, "year",4)
month_number: int = get_value(month, "month", 2)

while month_number not in range(1,13):
    print("Months mus be between 1 and 12 inclusive both")
    month_number: int = get_value(month, "month", 2)


print(month(year, month_number))
