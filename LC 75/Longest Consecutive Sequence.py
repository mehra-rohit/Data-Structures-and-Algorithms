# unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Pseudo Algo
# Track max sequence: compare next element with current it should be +1 or 0
## if +1 then +1 seq // if 0 seq +0

# compare current max with new seq length if seq breaks.

def long_cons_seq(nums: list[int]) -> int:
    max_seq = 1
    curr_seq = 1

    nums = sorted(nums, reverse=False)

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            curr_seq += 1
        elif nums[i] == nums[i - 1]:
            continue
        else:
            if curr_seq > max_seq:
                max_seq = curr_seq
                curr_seq = 1

    if curr_seq > max_seq:
        max_seq = curr_seq

    return max_seq


nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

assert long_cons_seq(nums1) == 4
assert long_cons_seq(nums2) == 9


# optimised
def lcs_op(nums: list[int]) -> int:
    nums_set = set(nums)
    lcs = 0

    for i in nums:
        # checking if i is a start of a sequence
        if i - 1 not in nums_set:
            l = 0
            while (i + l) in nums_set:
                l += 1
            lcs = max(lcs, l)
    return lcs


assert lcs_op(nums1) == 4
assert lcs_op(nums2) == 9
