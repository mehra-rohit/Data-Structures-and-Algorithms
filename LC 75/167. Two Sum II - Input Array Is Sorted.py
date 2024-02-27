# sorted array nums ascending
# given target find the index of two elements which sum up to target
# Your solution must use only constant extra space. (Use two pointer method in this case)
# [1,2,3,4,5] -> l+r > target (this means we need to move r pointer towards left)
# l+r > target (this means we need to move l pointer towards right)
# else -> we can say l+r == target and return [l,r]

def two_sum(arr: list[int], target: int) -> list[int]:

    l, r = 0, len(arr)-1
    while l < r:
        if arr[l] + arr[r] < target:
            l += 1
        elif arr[l] + arr[r] > target:
            r -= 1
        else:
            return [l, r]
    return [-1, -1]


numbers = [2, 7, 11, 15]
t = 9
t1 = 10

assert two_sum(numbers, t) == [0, 1]
assert two_sum(numbers, t1) == [-1, -1]






