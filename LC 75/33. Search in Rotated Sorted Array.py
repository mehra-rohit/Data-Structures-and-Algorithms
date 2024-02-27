"""
Search in rotated array

"""
"""
# rotated nums, target
# in normal binary search we compare mid with target and move pointers based on it.
# since left <= mid <= right
# in rotated array above condition will not hold true
# all cases in rotated array
1. nums[l] < nums[mid] left portion of the sorted array
    target < nums[mid] : r = mid - 1
    target > nums[mid] (target > nums[l] as well): l = mid + 1 
    target < nums[l] : l = mid + 1
    
2. nums[l] > nums[mid] # right portion of the sorted array
    target < nums[mid] (target < nums[r] as well): r = mid - 1
    target > nums[mid]: l = mid + 1
    target > nums[r]: r = mid - 1
    
array will be present in two parts left sorted + right sorted

"""


def search_rot_array(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        if nums[l] <= nums[mid]:
            if target < nums[l] or target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0

assert search_rot_array(nums1, target1) == 4
