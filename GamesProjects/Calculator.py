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
  first_number = None
  while not isinstance(first_number, (int, float)) :
    try:
       first_number = float(input("What's the first number?: "))
    except ValueError as e:
       print("Please enter a proper number")
  
  for key in operations:
      print(key)
  while not restart:
    operation = None
    while operation not in operations:
       operation =  input("Pick an operation: ")
    second_number = None
    while not isinstance(second_number, (int, float)):       
        try:
            second_number= float(input("What the next number?: "))
        except ValueError:
           print("Please enter a proper number")
    answer = operations[operation](first_number,second_number)
    print(f"{first_number} {operation} {second_number} = {answer}")
    keep= None
    while keep not in ('y', 'n', 'x'):
        keep=input(f"Type\n- 'y' to start a calculation from {answer}\n- 'n' to make a new one \n- 'x' to exit: ").lower()
    if keep == 'y':
      first_number = answer
    elif keep =='n':
      restart= True   
      calculation()
    else:
       break
calculation()