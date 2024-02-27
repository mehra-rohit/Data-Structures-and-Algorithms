# Given nums -> array, return all possible triplet element which sum up to zero.
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Algo : break the problem down to two sum, nums[i] + nums[j] = -nums[k]
# O(n) : N2


def three_sum(nums: list[int]) -> list[list[int]]:
    ans = []
    nums.sort()
    print(nums)

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            print(l,r)
            sum3 = nums[i] + nums[l] + nums[r]
            if sum3 > 0:
                r -= 1
            elif sum3 < 0:
                l += 1
            else:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return ans


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
