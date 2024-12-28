
user_operation, first_number, second_number = None, None, None

while user_operation not in ("+","/"):
    user_operation= input(f"For additon inser '+' for division insert '/' : ")
while not isinstance(first_number, (int, float)):
    first_number = input(f"Please insert the first number: ")
    try:
        first_number = float(first_number)
    except ValueError as e:
        print(e)
        print("Please enter a proper number")

while not isinstance(second_number, (int, float)):
    second_number = input(f"Please insert the second number: ")
    try:
        second_number = float(second_number)
    except ValueError as e:
        print(e)
        print("Please enter a proper number")

numbers = {"first": first_number, "second": second_number}


def addition(number_dic: dict) -> float:
    try:
        assert float(number_dic.get("first")), "The first number is not a number, Try again"
        assert float(number_dic.get("second")), "The second number is not a number, Try again"
        first_float = float(number_dic.get("first"))
        second_float = float(number_dic.get("second"))
    except ValueError as e:
        print("e")
    return first_float + second_float


def division(number_dic: dict) -> float:
    try:
        assert float(number_dic.get("first")), "The first number is not a number, Try again"
        assert float(number_dic.get("second")), "The second number is not a number, Try again"
        first_float = float(number_dic.get("first"))
        second_float = float(number_dic.get("second"))
    except ValueError as e:
        print("e")
    return first_float / second_float


all_operations = {"+": addition(numbers), "/": division(numbers)}

print(all_operations.get(user_operation))