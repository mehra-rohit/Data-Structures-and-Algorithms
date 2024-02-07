# arr = [2,3,7,8,10]
# target = 11
# return if there exists a subset of array which sums up to target.

# Recursive solution
# base condition
# when sum = 0 ; True

# Choice Diagram
# when item i <= target ; Include or not include in subset
# when item i> target ; Not include in subset

def subset_sum(arr: list[int], target: int, n: int):
    if target == 0:
        return True
    elif n == 0:
        return False
    if arr[n - 1] <= target:
        return subset_sum(arr, target - arr[n - 1], n - 1) | subset_sum(arr, target, n - 1)
    elif arr[n - 1] > target:
        return subset_sum(arr, target, n - 1)


arr = [2, 3, 7, 8, 10]
assert (subset_sum(arr=arr, target=11, n=len(arr)))
assert (subset_sum(arr=arr, target=10, n=len(arr)))
assert (subset_sum(arr=arr, target=100, n=len(arr)) == False)


# Memoized solution
def subset_sum(nums: list[int], val: int, n: int) -> bool:
    if val == 0:
        return True
    elif n == 0:
        return False

    if t[n][val] != -1:
        return t[n][val]

    if nums[n - 1] <= val:
        t[n][val] = subset_sum(nums, val - nums[n - 1], n - 1) | subset_sum(nums, val, n - 1)
    elif nums[n - 1] > val:
        t[n][val] = subset_sum(nums, val, n - 1)

    return t[n][val]


arr = [2, 3, 7, 8, 10]
target = 11
n_ = len(arr)
t = [[-1 for i in range(target+1)] for j in range(n_+1)]

assert subset_sum(nums=arr, val=target, n=n_)


# Top Down Solution (Iterative Solution)
# Initialise base case in table
# Remove recursion calls
def subset_sum(nums: list[int], val: int, n: int) -> bool:
    # First row will be False
    # First column will be True
    t = [[-1 for i in range(val + 1)] for j in range(n + 1)]
    for i in range(target + 1):
        t[0][i] = False
    for i in range(n):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, target+1):
            if nums[i-1] <= j:
                t[i][j] = t[i-1][j-nums[i-1]] | t[i-1][j]
            elif nums[i-1] > j:
                t[i][j] = t[i-1][j]

    return t[n][val]


arr = [2, 3, 7, 8, 10]
target = 30
assert subset_sum(nums=arr, val=target, n=len(arr)) == True
