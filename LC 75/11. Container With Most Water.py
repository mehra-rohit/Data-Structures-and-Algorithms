"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""


# brute force
def max_water(nums: list[int]) -> int:
    res = 0

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            h = min(nums[i], nums[j])
            area = h * (j - i)
            if area > res:
                res = area
    return res


def max_water_op(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    res = 0
    while l < r:
        h = min(nums[l], nums[r])
        area = h * (r - l)
        res = max(area, res)
        if nums[l] <= nums[r]:
            l += 1
        else:
            r -= 1

    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
assert max_water(height) == 49
assert max_water_op(height) == 49
