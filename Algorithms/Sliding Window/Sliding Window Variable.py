# Find the length of the longest subarray, with the same value in each position

# Iterate over the loop
# check if right pointer value is equal to left point
#   true -> do nothing
#   false -> update left pointer to right pointer
# check if current max_length is smaller than new length

def sliding_window_var(nums: list[int]) -> int:
    L = 0
    length = 0

    for R in range(len(nums)):
        if nums[R] != nums[L]:
            L = R

        length = max(length, R - L + 1)

    return length


nums1 = [1, 2, 2, 3, 3, 3]
assert sliding_window_var(nums1) == 3


# Find the minimum length subarray, where the sum is greater than or equal to the target.
# Assume all values are positive (hint about the solution)

"""
sliding window solution

Note : In this problem we want to minimise so choose ans or min_length as max value initially
        -> Max value would be float('inf') or we can take len(nums) + 1 as ans will be smaller than this.
target = 6
nums = [2, 3, 1, 2, 4, 3]

1. Iterate over the array
2. Check for the condition
    -> If sum is less than target
        -> True add the right pointer value
    -> Removal condition check
        -> We keep removing items from left till the sum is greater than target
        -> Keep updating length 

var needed: left pointer, window sum, ans
"""


def min_subarray(nums: list[int], target: int) -> int:

    L, curr_sum = 0, 0
    length = len(nums)+1

    for R in range(len(nums)):
        curr_sum += nums[R]

        while curr_sum >= target:
            length = min(length, R - L + 1)
            curr_sum -= nums[L]
            L += 1

    return length if length != len(nums) + 1 else 0


target1 = 6
nums1 = [2, 3, 1, 2, 4, 3]

assert min_subarray(nums1, target1) == 2


