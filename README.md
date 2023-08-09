# Python-Project-Portfolio
This repository contains my Python Project Portfolio

```python
def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculation():
  restart= False
  first_number = float(input("What's the first number?: "))
  for key in operations:
      print(key)
  while not restart:
    operation =  input("Pick an operation: ")
    second_number= float(input("What the next number?: "))
    answer = operations[operation](first_number,second_number)
    print(f"{first_number} {operation} {second_number} = {answer}")
    keep=input("Type 'y' to start a calculation from {answer} or make 'n' to make a new one : ").lower()
    if keep == "y":
      first_number = answer
    else:
      restart= True   
      calculation()
calculation()

```
