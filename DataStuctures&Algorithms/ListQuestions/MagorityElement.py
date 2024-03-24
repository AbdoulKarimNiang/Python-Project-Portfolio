# A Majority Elemnt is an element that is repeated more than half on the number of element.

# Best Solution
import math

arr = [2, 2, 1, 1, 2, 2, 3, 4, 2, 2, 2]


class Solution(object):
    def majorityElement(self, nums):
       nums.sort()
       position= int(math.floor(len(nums)/2))
       return nums[position]


s1: Solution = Solution()
print(s1.majorityElement(arr))


# Good Approach

arr = [2, 2, 1, 1, 2, 2, 3, 4, 2, 2, 2]


class Solution(object):
    def majority_element(self,nums: list[int]) -> int:
        count = 0
        majority = None
        for num in nums:
            if count == 0:
                majority = num
            if majority != num:
                count = count - 1
            else:
                count = count + 1
        return majority


# Brute Force
arr = [2, 2, 1, 1, 2, 2, 3, 4, 2, 2, 2]


class Solution:
    def majority(self, nums: list[int]) -> int:
        counting = {}
        for i in range(len(nums)):
            current = nums[i]
            counting.setdefault(current, 0)
            counting[current] += 1
        majority_element = max(counting, key=lambda x: counting[x])
        return majority_element


s1: Solution = Solution()
print(s1.majority(arr))

