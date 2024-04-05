# Center 
string: str = "Main Menu"
width = 300
print(f"{string:_^{width}}")


# Round a number
from random import random, randint

string: str = "Main Menu"
width = 300
print(f"{string:_^{width}}")

rando_int: int = randint(0, 100)
random_float: float = random()
final_number = random_float * rando_int
print(f"{final_number:,.2f}")



# Multiline f-strings (DocString)
formatted_string = f"""
Name: {name}
Age: {age}
"""
print(formatted_string)


