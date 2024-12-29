
limit = None
while not isinstance(limit, (int, float)):
    try:
        limit: int = int(input(f"Please insert the upper limit: "))
    except ValueError as e:
        print(e)
        print("Insert a valid number")

total: int = 0
for i in range(1,limit+1):
    total+= i

print(total)
