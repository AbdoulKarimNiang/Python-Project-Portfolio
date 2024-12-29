
def get_number(value: None|str, name: str)-> int:
    while not isinstance(value, (int, float)):
        try:
            value: int = int(input(f"Please insert the {name} number: "))
        except ValueError as e:
            print(e)
            print("Insert a valid number")
        return value

def less_common_multiple(x: int, y: int):
    greater = max(x, y)
    while True:
        if (greater % x == 0) and (greater % y == 0):
            print(f"The Less common multiple is {greater}")
            break
        else:
            greater += 1

x = None
y = None
x: int = get_number(x, "first")
y: int = get_number(y, "second")

less_common_multiple(x, y)
