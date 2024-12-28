a = input(f"insert the variable a: ")
b = input(f"insert the variable b: ")

c = a
a = b
b = c
del c

print(f"The variable a now is {a} and the variable b is now {b}")
