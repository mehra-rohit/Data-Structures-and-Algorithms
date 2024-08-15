'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
'''

from typing import List

nums = [3,4,5,6]
target = 7

# time -> O(n2), Space -> O(1)
def twoSum(nums: List[int], target: int) -> List[int]:

    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums):
            if i == j:
                continue

            if n1 + n2 == target:
                return [i, j]
            

assert twoSum(nums, target) == [0,1] 

# time -> O(n), Space -> O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
    temp = {}

    for i, num in enumerate(nums):
        if target - num in temp:
            return [temp[target - num], i]

        temp[num] = i  

assert twoSum(nums, target) == [0,1] 