'''
The Prefix Sums algorithm is a common technique used in various algorithms to compute cumulative sums or ranges of sums efficiently. 
It is particularly useful when you need to perform multiple queries on a data set to determine the sum of elements between two indices 
or when you want to preprocess data to make sum queries faster.

What is a Prefix Sum?
A Prefix Sum is the cumulative sum of the elements of an array up to a certain index. 
For an array nums, the prefix sum at index i is the sum of all elements from the beginning of the array up to the index i.
'''

'''
Applications of Prefix Sums

Range Sum Queries: 
Prefix sums are often used to answer range sum queries efficiently. 
For example, to find the sum of elements between indices i and j in the array, you can compute it as:

Cumulative Frequency:
In problems where you need to calculate the cumulative frequency or probability, prefix sums provide an efficient way to do this.

Finding Subarrays with a Given Sum: 
You can use prefix sums to find subarrays that sum up to a given value, by storing prefix sums in a hash map and checking for differences.

'''


# How to compute Prefix Sum

from typing import List

def prefix_sum(nums: List[int]) -> List[int]:
    prefix = []
    total = 0
    for i in nums:
        total += i
        prefix.append(total)

    return prefix


# find sum of a subarray

def rangesum(nums: List[int], i: int, j: int) -> int:
    prefix = prefix_sum(nums)

    left = prefix[i-1] if i > 0 else 0
    if j < len(nums):
        right = prefix[j]
    else:
        return 'right index must be less than lenght of array'

    return right - left


nums = [1,2,3,4]

assert rangesum(nums, 0, 1) == 3
assert rangesum(nums, 0, 0) == 1

assert rangesum(nums, 1, 3) == 9

print(rangesum(nums, 1, 5))