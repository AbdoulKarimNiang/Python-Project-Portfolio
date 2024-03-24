# Brute Force
numbers = [1, 5, 8, 4, 9, 3, 18, 2]

lunghezza = len(numbers)

indice = 0
target = 22
for i in range(0, lunghezza):
    for y in range(i, lunghezza):
        if total := numbers[i] + numbers[y] == target:
            print([i, y])
        else:
            pass
