number = None
while not isinstance(number, (int, float)):
    try:
        number = int(input(f"Please insert a valid number: "))
    except ValueError as e:
        print("You didn't inset a valid number")

total = 0

string_number = str(number)
number_digits = len(string_number)
for digit in string_number:
    value = int(digit) ** number_digits
    total += value

if total == int(number):
    print(f"{number} it's an Amstrong number!")
else:
    print(f"{number} it's not an Amstrong number!")
