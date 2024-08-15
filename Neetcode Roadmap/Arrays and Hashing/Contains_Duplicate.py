'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
'''

from typing import List

nums1 = [1, 2, 3, 3]
nums2 = [1, 2, 3]

# Quick Solution to know if there is an duplicate, but doesnot tell which element is duplicate. Time Complexity -> O(n), Space Complexity -> O(n)
'''
The conversion to a set is O(n) because it requires processing each element of the list.
In Python, retrieving the length of a list is an O(1) operation because the length is stored as an attribute of the list object.
The comparison of lengths is O(1) because it's simply a direct comparison of two integers.
The total space complexity of the function is O(n) because of the space required to store the set set(nums).
'''
def hasDuplicate(nums: List[int]) -> bool:

    return len(nums) == len(set(nums))


assert hasDuplicate(nums1) == False
assert hasDuplicate(nums2) == True

# Ideal solution as using this we can find the duplicate element as well. Time -> O(n), Space -> O(n)
'''
temp initialisation is O(1)
Iterating through loop is O(n)
num check in temp is O(1) because sets are implemented as hash tables
Element addition in temp is O(1)
'''
def hasDuplicate(nums: List[int]) -> bool:
    temp = set()

    for num in nums:
        if num in temp:
            return True
        temp.add(num)

    return False

assert hasDuplicate(nums1) == True
assert hasDuplicate(nums2) == False