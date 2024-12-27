from calendar import month

year = None
month_number = None

def get_value(value, name:str, digits_number: int) -> int:
    while not isinstance(value, (int, float)) :
        try:
            value: int = int(input(f"Please insert the {name} in {digits_number} digits: "))
        except ValueError as v:
            print(v, "Please insert a valid numeric value")
            print(f"The value must have exactly {digits_number} digits.")
        
    return value

year: int = get_value(year, "year",4)
month_number: int = get_value(month, "month", 2)

while month_number not in range(1,13):
    month_number: int = get_value(month, "month", 2)


print(month(year, month_number))
