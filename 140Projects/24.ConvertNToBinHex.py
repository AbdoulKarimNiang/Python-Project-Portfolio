# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

# Converting a decimal number to binary, octal, and hexadecimal involves dividing the
# decimal number by the base repeatedly and noting the remainders at each step.


def get_number(value: None|str)-> int:
    while not isinstance(value, (int, float)):
        try:
            value: int = int(input(f"Please insert the value to convert: "))
        except ValueError as e:
            print(e)
            print("Insert a valid number")
    return value


def convert_binary(value: int) -> str:
    flag: bool = True
    binary_str: str = ''
    while flag:
        quotient = int(value / 2)
        remainder : int = value % 2
        binary_str+= str(remainder)
        value = quotient
        if quotient == 0 :
            flag = False
    return binary_str


HEX = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f'
}

def convert_hex(value: int) -> str:
    hex_string = ''
    remainder = None
    while True:
        quotient = int(value / 16)
        remainder : int = value % 16
        hex_string +=str(quotient)
        if remainder in HEX:
            new_hex = HEX.get(remainder)
            hex_string +=str(new_hex)
            break
        if quotient == 0:
            break
    return hex_string

def convert_oct(value)-> str:
    flag: bool = True
    oct_sting = ''
    while flag:
        quotient = int(value / 8)
        remainder : int = value % 8
        oct_sting+= str(remainder)
        value = quotient
        if quotient == 0:
            flag = False
    return oct_sting


x = None
x = get_number(x)

user_input: str =input("Do you want to convert it in Binary 'b', Hexadecimal 'h', or Octal 'o'?: ").lower()
if user_input == 'b':
    binary_value = convert_binary(x)
    print(f"The number {x} in Binary is {binary_value}")
    check_value = int(binary_value, 2)

    if x == check_value:
        print("The conversion is successfull")
    else:
        print("Something gone wrong in the convertion, the value provided is not correct")
elif user_input == 'h':
    hex_value: str = convert_hex(x)
    print(f"The number {x} in Hexadecimal is {hex_value}")
elif user_input == 'o':
    oct_value: str = convert_oct(x)
    print(f"The Octal representation of the number {x} is {oct_value}")



