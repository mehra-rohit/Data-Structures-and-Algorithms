# arr = [1, 5, 11, 5]
# output = True/False
# Given an array find if their we can partition the array such that both partition have equal sum
# Solution : This problem can be converted to subset_sum_problem
# arr -> arr1 + arr2 ; sum(arr1)==sum(arr2) ; if sum(arr1) = S, sum(arr) becomes 2S,
# This means sum of main array should be even otherwise it cannot have equal sum partition
# In subset_sum_problem we find if the array has a subset array with sum equals to target
# In this case array will be same and target becomes S which is sum(arr)/2

def subset_sum(nums: list[int], target: int, n: int) -> bool:
    # create dp table
    t = [[-1 for i in range(target+1)] for j in  range(n+1)]
    # initialize base condition
    # sum = 0 will be true and n = 0 will be false
    for i in range(target+1):
        t[0][i] = False
    for i in range(n+1):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, target+1):
            if nums[i-1] <= j:
                t[i][j] = t[i-1][j-nums[i-1]] | t[i-1][j]
            elif nums[i-1] > j:
                t[i][j] = t[i-1][j]
    return t[n][target]


def equal_sum_partition(nums: list[int]) -> bool:
    s = 0
    for i in nums:
        s += i
    if s % 2 == 0:
        return subset_sum(nums, int(s/2), len(nums))
    else :
        return False


arr = [1, 5, 11, 5]

assert equal_sum_partition(arr) == True





