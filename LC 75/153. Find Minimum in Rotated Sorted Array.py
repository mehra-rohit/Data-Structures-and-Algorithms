"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1],
 a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
"""


# if nums[l] > nums[r] -> min val is still in mid or at r, we move left pointer to mid + 1
# otherwise if nums[l] < nums[r] -> 51234 in this case we move right pointer to mid - 1


def min_rotated_sort_array(nums: list[int]) -> int:
    ans = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            ans = min(ans, nums[l])
            break
        mid = (l + r) // 2
        ans = min(ans, nums[mid])
        if nums[l] < nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return ans


def max_rotated_sort_array(nums: list[int]) -> int:
    ans = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            ans = max(ans, nums[r])
            break
        mid = (l + r) // 2
        ans = max(ans, nums[mid])
        if nums[l] <= nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return ans


nums1 = [1, 2, 3, 4, 5]
nums2 = [4, 1, 2, 3]
nums3 = [4, 5, 6, 7, 0, 1, 2]

assert min_rotated_sort_array(nums1) == 1
assert min_rotated_sort_array(nums2) == 1
assert min_rotated_sort_array(nums3) == 0
assert max_rotated_sort_array(nums3) == 7
