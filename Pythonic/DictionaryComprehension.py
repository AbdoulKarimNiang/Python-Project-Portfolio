# Exercise 1: Basic Dictionary
# Create a dictionary comprehension that squares each number from 1 to 5 and stores it as key-value pairs.

squared_dictionary = {key: key * 2 for key in range(0, 6)}
print(squared_dictionary)

# Exercise 2: Even-Odd Mapping
# Generate a dictionary comprehension that maps numbers from 1 to # 10
# to "even" if they're even and "odd" if they're odd.

even_odd_dictionary = {key: "Even" if key % 2 == 0 else "Odd" for key in range(0, 10)}
print(even_odd_dictionary)

# Exercise 3: Word Lengths
# Given a list of words, create a dictionary comprehension that
# maps each word to its length.

my_sentence = "This is the string for which calculate frequency"
word_length = {key: len(key) for key in my_sentence.split(" ")}
print(word_length)

# Exercise 4: Filtered Dictionary
# Create a dictionary comprehension that filters out key-value # pairs from an existing dictionary
# where the value is greater than 5.

my_existing_dictionary = { 'value1': 21,
                            'value2': 30,
                            'value3': 1,
                            'value4': 5,
                            'value5': 7}

new_dictionary_filtered = {key: value for key, value in my_existing_dictionary.items() if value > 5}
print(new_dictionary_filtered )

# Exercise 5: Nested Dictionary Comprehension
# Given two lists, one containing names and the other containing # # ages, create a dictionary comprehension to create a dictionary # of names as keys and ages as values.

names = ['Luca', 'Alessio', 'Marco', "Giovanni", 'Karim']
ages = [33, 44, 42, 67, 37]
zipped = zip(names, ages)
names_ages_dictionary = {name: age for name, age in zipped}
print(names_ages_dictionary)

# Exercise 6: Unique Letters Count
# Write a dictionary comprehension that takes a sentence as input and creates a dictionary
# with letters as keys and their counts as values (ignoring spaces and considering case-insensitivity).

word_count_dict ={char: my_sentence.count(char) for char in my_sentence.strip()}
print(word_count_dict)


# Exercise 7: Flattening Nested Dictionaries
# Given a nested dictionary, create a dictionary comprehension
# to flatten it into a single-level dictionary where the keys are tuples of the original keys.

nested_dictionary = {"outer_key1":
                         {"inner_key1": "inner_value1"},
                    "outer_key2":
                         {"inner_key2": "inner_value2"},
                    "outer_key3":
                            {"inner_key3": "inner_value3"}
}


flatter_dictionary = {(outer_key, outer_value): inner_value
                      for outer_key, outer_value in nested_dictionary.items()
                      for outer_value, inner_value in outer_value.items()}
print(flatter_dictionary)

# Exercise 8: Dictionary of Squares
# Generate a dictionary comprehension that maps numbers from 1 to 10 to their squares, but only for even numbers.

square_of_even_numbers = {f"number {num}": num*num for num in range(1,11) if num % 2 == 0}
print(square_of_even_numbers)

# Exercise 9: Letter Frequency
# Write a dictionary comprehension that takes a string as input and creates a dictionary with letters
# as keys and their frequency in the string as values.

the_string = "This is the string for which calculate frequency"
string_frequency = {char: the_string.count(char) for char in the_string if char.isalpha()}
print(string_frequency)

