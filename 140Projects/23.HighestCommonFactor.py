#HCF, or Highest Common Factor, is the largest positive integer 
# that divides two or more numbers without leaving a remainder.


def get_number(value: None|str, name: str)-> int:
    while not isinstance(value, (int, float)):
        try:
            value: int = int(input(f"Please insert the {name} number: "))
        except ValueError as e:
            print(e)
            print("Insert a valid number")
    return value

def highest_common_factor(x: int, y: int):
    lower = min(x, y)
    highest_common_factor = 0
    for i in range(1, lower + 1):
        if (x % i == 0) and ((x % i == 0)):
            highest_common_factor = i
    return highest_common_factor


x = None
y = None
x: int = get_number(x, "first")
y: int = get_number(y, "second")

highest_common_factor = highest_common_factor(x, y)

print(f"The highest common factor is {highest_common_factor}")