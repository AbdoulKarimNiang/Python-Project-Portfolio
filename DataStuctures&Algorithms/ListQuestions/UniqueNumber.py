# Best Aproach

from typing import List
numbers = [4, 2, 4, 2, 7, 1, 1]

class Solution:
    def find_single_number(self,nums:List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

s1: Solution = Solution()
single =s1.find_single_number(numbers)
print(f"The single number in the list is: {single}")



# Brute Force
from typing import List

numbers = [3, 6, 7, 6, 7]

number_dictionary = {}


class Solution:
    def find_unique(self,numbers: List[int]) -> int:
        for number in numbers:
            if number in number_dictionary:
                number_dictionary[number] = number_dictionary[number] + 1
            else:
                number_dictionary.setdefault(number, 1)
        for number in number_dictionary.keys():
            if number_dictionary[number] > 1:
                pass
            else:
                final_number = number
                return final_number


s1 = Solution()
print(s1.find_unique(numbers))
