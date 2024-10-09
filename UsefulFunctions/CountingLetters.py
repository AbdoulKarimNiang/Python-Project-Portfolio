string = f" A very long sentence that I can't recall"

letters = {}
for char in string:
    letters.setdefault(char, 0)
    letters[char] += 1

print(letters)
