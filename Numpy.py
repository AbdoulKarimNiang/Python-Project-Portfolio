import random

import numpy as np

# 1. Create a NumPy array with values 1 to 5.
five_array = np.array(range(6))
print(five_array)
print(type(five_array))
help(np)

# 2. Create a 3x3 matrix with all zeros
zero_array_x3 = np.zeros((3, 3))
print(zero_array_x3)

# 3. Generate an array of 10 random numbers between 0 and 1
random_10_number = np.random.rand(10)
print(random_10_number)

# 3. Multiply a 3x3 matrix by a scalar value.

integer_array_x3 = np.random.randint(low=1, high=100, size=(3, 3))
random_integer = random.randint(10, 50)
print(integer_array_x3)
print(int(random_integer))
integer_array_x3_result = integer_array_x3 * random_integer
print(f"The result of: \n{integer_array_x3} * {random_integer} =\n {integer_array_x3_result}")

# 4. Reshape a 1D array to a 3x3 grid.
array_12_elements = np.arange(9)
array_12_elements_reshaped = array_12_elements.reshape(3, 3)
print(array_12_elements_reshaped)

# 5. Concatenate two arrays vertically.
first_array = np.arange(5)
second_array = np.array(range(1, 10, 2))
print(np.vstack((first_array, second_array)))

# 6. Extract all odd numbers from an array.

# 6.1 First attempt
array_for_odds = np.arange(100)
new_list_for_odds = []
for i in array_for_odds.flat:
    if i % 2 != 0:
        new_list_for_odds.append(i)
# overwrite existing one
array_for_odds = np.array(new_list_for_odds)
print(array_for_odds)

# 6.2 Second attempt with list comprehension

second_array_from_odds = np.array([i for i in range(100) if i % 2 != 0])
print(second_array_from_odds)

# 6.3 Compute the mean, median, and standard deviation of an array.

base_array = np.arange(74)
print(base_array.mean())
print(base_array.std())
print(np.median(base_array))

# 7. Append arrays.
first_array = np.arange(5)
second_array = np.array(range(1, 10, 2))
combined_array = np.vstack((first_array, second_array))
print(combined_array)

# 8. Transpose a matrix.
print(np.transpose(combined_array))
