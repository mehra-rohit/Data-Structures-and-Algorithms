'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.
'''

nums = [2,20,4,10,3,4,5]
output = 4

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    sorted_nums = sorted(nums)

    lcs = 0
    temp = 1
    for i in range(0, len(sorted_nums) - 1):
        if sorted_nums[i] + 1 == sorted_nums[i + 1]:
            temp += 1
        elif sorted_nums[i] == sorted_nums[i + 1]:
            continue
        else:
            if temp > lcs:
                lcs = temp
            temp = 1

    if temp > lcs:
        lcs = temp

    return lcs

assert longestConsecutive(nums) == output

def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    lcs = 0

    for num in nums:
        # check if num is start of a sequence
        if num - 1 not in nums_set:
            l = 0
            while num + l in nums_set:
                l += 1
            lcs = max(l, lcs)

    return lcs

assert longestConsecutive(nums) == output


'''
Why It's Still O(n)

1. Each Element is Processed Once in the while Loop:

The while loop does not revisit any element that has already been part of a sequence. 
Once a number is found and processed in a sequence, it won’t be the start of another sequence in any future iterations of the for loop.
For example, if the sequence is [1, 2, 3, 4], when the for loop hits 1, the while loop will process 1, 2, 3, and 4. 
However, when the for loop gets to 2, 3, or 4, the while loop won't run because num - 1 (i.e., 1, 2, 3) is in nums_set.

2. Total Number of Operations:

Across the entire execution of the function, each element in nums is part of the while loop at most once. 
This means that even though the while loop is nested inside the for loop, the total number of operations performed by the while loop is limited to O(n)

'''

