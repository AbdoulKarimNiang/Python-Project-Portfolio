# Best Approach

from typing import List

numbers = [1, 5, 8, 4, 9, 3, 18, 2]
target = 22

class Solution:
   def twoSum(nums: List[int], target: int) -> List[int]:
        my_value_dictio = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in my_value_dictio:
                return [i, my_value_dictio[compliment]]
            else:
                my_value_dictio[num] = i

s1 = Solution()
print(s1.twoSum(numbers,target))



# Good Aproach

 from typing import List
 class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         new_nums = nums.copy()
         new_nums.sort()
         i = 0
         j = len(nums) - 1
         while (i < j):
             if(new_nums[i] + new_nums[j] == target):
                 if (new_nums[i] == new_nums[j]):
                 	return [nums.index(new_nums[i]),nums.index(new_nums[j],nums.index(new_nums[i])+1)]
                 else:
                 	return [nums.index(new_nums[i]),nums.index(new_nums[j])]
             elif (new_nums[i] + new_nums[j] < target):
             	i = i + 1
             else:
             	j = j - 1
 s1 = Solution()
 s1.twoSum([1,5,8,4,9,3,18,2],27)

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

