# arr = [1, 1, 2, 4]
# diff = 1
# Find number of subsets whose sum diff is equal to give diff.
# arr -> arr1, arr2;
# s1 - s2 = diff
# s1 + s2 = s
# adding above equation we get, 2s1 = diff+s: s1 = (diff+s)/2
# we use subset_sum logic here to count number of subset which have sum = s1 or (diff - s)/2

def count_subset_sum(nums: list[int], val: int, n: int) -> int:

    # dp table
    t = [[-1 for i in range(val+1)] for j in range(n+1)]
    # initialise base condition, when sum = 0, make it 1 and if n=0 and sum>0 make it 0
    for i in range(val+1):
        t[0][i] = 0
    for i in range(n+1):
        t[i][0] = 1

    # run iteration after initialised values
    for i in range(1, n+1):
        for j in range(1, val+1):
            if nums[i-1] <= j:
                t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
            elif nums[i-1] >j:
                t[i][j] = t[i - 1][j]
    return t[n][val]


def count_subset_diff(nums: list[int], diff: int) -> int:

    s = 0
    for i in nums:
        s += i

    s1 = (s+diff)/2
    if (s+diff) % 2 == 0:
        return count_subset_sum(nums, int(s1), len(nums))
    else:
        return 0


assert count_subset_diff(nums=[1, 1, 2, 3], diff=1) == 3
assert count_subset_diff(nums=[1, 1, 2, 3], diff=2) == 0
