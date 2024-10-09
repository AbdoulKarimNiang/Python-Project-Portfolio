from collections import Counter, defaultdict, deque, namedtuple
from random import randint

# Write a function that takes a list of integers and returns the count of each unique integer using Counter.

numbers = [randint(0,8) for i in range(30+1)]

def count_occurences(values: list[int]) -> dict:
    counter = Counter(values)
    return counter

print(count_occurences(numbers))


# Given a string of text, use Counter to find the top 3 most common words.

from string import ascii_letters

lenght_string = len(ascii_letters) - 1

random_string = [ ascii_letters[randint(0, lenght_string)] for i in range(0,30)]

random_string = "".join(random_string)
counter_word_string = Counter(random_string)

print(counter_word_string.most_common(3))



# 3. Default Values with defaultdict
## Create a defaultdict where the default value for non-existing keys is an empty list. Add multiple values to a key in the dictionary.

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
d['b'].append(4)

# dict_items([('a', [1, 2]), ('b', [3, 4])])

print(d.items())

# setting the default value allows you to perform basic data type operation without taking 
# in consideration the absence of the value like you would do with normal dictionary using setdefault

# indeed the below code throw an error 
# normal_dictionary = {}

# normal_dictionary['a'].append(1)
# normal_dictionary['a'].append(2)
# normal_dictionary['b'].append(3)
# normal_dictionary['b'].append(4)

# Traceback (most recent call last):
#   File "c:\Users\karim.niang\Desktop\VsPythonCode\PythonScript\GettingStartedWithCollections.py", line 47, in <module>
#     normal_dictionary['a'].append(1)
#     ~~~~~~~~~~~~~~~~~^^^^^


## 4. Word Lengths with defaultdict
## Write a program that categorizes words from a list by their length using defaultdict.

sentence = 'this is a basic sentence for word lenght calculation using default dict'

sentence_dictionary = defaultdict(list)

def word_lenght_mapping(value: str) -> dict:

    list_word = sentence.split(' ')
    for word in list_word:
        word_lenght = len(word)
        sentence_dictionary[word_lenght].append(word) 
    return sentence_dictionary

print(word_lenght_mapping(sentence))

# 5. Double-ended Queue (deque)
## Implement a queue using deque. Add and remove elements from both ends, and print the final state of the deque.

q = deque('bcd')
q.appendleft('e')
q.append('a')

print(q)
# result deque(['e', 'b', 'c', 'd', 'a'])
q.pop()
q.popleft()

print(q)

# result deque(['b', 'c', 'd'])


## 6. Rotate a Deque
## Create a deque with integers from 1 to 10. Rotate the deque three times to the right and print the result.

integer_deque = deque(range(0,11))
integer_deque.rotate()
print(integer_deque)

# resul deque([10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

## 7. Named Tuple
## Create a namedtuple called Point with fields x and y. Write a function that takes two points and calculates the distance between them.


Point = namedtuple('Point', ['x', 'y'])


def distance( a: int, b:int) -> int:
    c = b - a
    return c

print(distance(namedtuple.x, namedtuple.y))


## 8. Storing Person Information with namedtuple
## Create a namedtuple called Person with fields like name, age, and city. Use it to store information about multiple people and print their details.

## 9. Ordered Dictionary
## Write a program that reads a list of tuples, where each tuple contains a key-value pair. Store the pairs in an OrderedDict and print them in the order they were added.

## 10. Moving Average with deque