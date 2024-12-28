

# quadratic formula (−b ± (b^2 − 4ac )^1/2)/(2a)

try:
    a = float(input("Give the variable a: "))
    b = float(input("Give the variable b: "))
    c = float(input("Give the variable c: "))

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        Root1 = (-b + discriminant ** (1 / 2)) / (2 * a)
        Root2 = (-b - discriminant ** (1 / 2)) / (2 * a)
        print(f"Root1 {Root1}, Root2 {Root2}")
    elif discriminant == 0:
        Root = -b / (2 * a)
        print(f"Root: {Root}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = (abs(discriminant) ** (1 / 2)) / (2 * a)
        print(f"Root 1: {real_part} + {imaginary_part}i")
        print(f"Root 2: {real_part} - {imaginary_part}i")
except ValueError as v:
    print(v, f"Please insert a valid number or a real number!")
