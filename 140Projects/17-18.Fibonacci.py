
start: int = 0
next: int = 1

result: int = 0

stop: int = 300

results_list: list[int] = []

while start + next < stop:
    result: int = start + next
    results_list.append(result)
    start = next
    next = result

print(results_list)
