# arr = [2, 3, 5, 6, 8, 10]
# sum = 10
# Find number of distinct subset which have sum equal to given sum
# we can leverage subset_sum here. Instead of computing true/false, add 1 everytime match is found in the dp table.

def count_of_subset_sum(nums: list[int], target: int, n: int) -> int:
    t = [[-1 for i in range(target + 1)] for i in range(n + 1)]
    # initialize DP Table with 1/0 for base condition.
    # if sum = 0, then there will be empty subset [] which will have sum 0, so return 1
    # if n = 0 and sum >0, then since empty subset [] sum is zero, condition will fail and we return 0

    for i in range(target + 1):
        t[0][i] = 0
    for i in range(n + 1):
        t[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                t[i][j] = t[i - 1][j - nums[i - 1]] + t[i - 1][j]
            elif nums[i - 1] > j:
                t[i][j] = t[i - 1][j]
    return t[n][target]


arr = [2, 3, 5, 6, 8, 10]
val = 10

assert count_of_subset_sum(nums=arr, target=val, n=len(arr)) == 3
