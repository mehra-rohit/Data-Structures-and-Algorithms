# arr = [1, 6, 11, 5]
# partition arr in such a way that difference of sum of two partition is minimum.
# arr -> arr1, arr2,
# S1 = sum(arr1), S2 = sum(arr2), S = sum(arr), S2 = S - S1
# objective minimize(abs(S - 2S1))
# S1 can range from (0,S). Check between 0,S using subset_sum if there is subset array with sum equal to val.
# We get list of possible S1 values then we find minimum using S - 2S1 relation.


def subset_sum(nums: list[int], val: int, n: int) -> bool:

    t = [[-1 for i in range(val+1)] for i in range(n+1)]
    # base condition initialisation
    for i in range(val+1):
        t[0][i] = False
    for i in range(n+1):
        t[i][0] = True

    # runs iteration for row, column after initialized values
    for i in range(1,n+1):
        for j in range(1,val+1):
            if nums[i-1] <= j:
                t[i][j] = t[i-1][j-nums[i-1]] | t[i-1][j]
            elif nums[i-1] > j:
                t[i][j] = t[i-1][j]
    return t[n][val]


def min_subset_sum(nums: list[int]) -> int:

    s = 0
    for i in range(len(nums)):
        s += nums[i]

    # range of s1 is (0,s)
    v = [False for i in range(0,s+1)]
    min_ss = s
    for target in range(len(v)):
        v[target] = subset_sum(nums, target, len(nums))

        if v[target]:
            min_ss = min(min_ss, abs(s-2*target))

    return min_ss


assert min_subset_sum(nums=[1, 6, 11, 5]) == 1
assert min_subset_sum(nums=[1, 5, 11, 5]) == 0  # equal partition case
