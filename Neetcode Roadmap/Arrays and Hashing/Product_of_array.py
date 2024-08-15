'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
Follow-up: Could you solve it in O(n)
O(n) time without using the division operation?
'''

from typing import List

nums = [1,2,4,6]

# time -> O(n), space -> O(n)
def productExceptSelf(nums: List[int]) -> List[int]:

    ans = [1 for i in range(len(nums))]
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            ans[j] *= nums[i]

    return ans


assert productExceptSelf(nums) == [48,24,12,8]


# time -> O(n), space -> O(n)
def productExceptSelf(nums: List[int]) -> List[int]:

    ans = [1 for i in range(len(nums))]
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            ans[j] *= nums[i]

    return ans


assert productExceptSelf(nums) == [48,24,12,8]


# Using Prefix sum
def productExceptSelf(nums: List[int]) -> List[int]:
    ans = []
    total = 1
    pre = []
    for i in nums:
        pre.append(total)
        total *= i
        

    # [1, 1, 2, 8]

    total = 1
    post = []
    for i in range(len(nums)- 1, -1, -1):
        post.append(total)
        total *= nums[i]
        
    # [1, 6, 24, 48]
    for i in range(len(nums)):
        left = pre[i]
        right =  post[len(nums)-1-i]

        ans.append(left*right)

    return ans
# print(productExceptSelf(nums))
assert productExceptSelf(nums) == [48,24,12,8]

# further can be simplified 
def productExceptSelf(nums: List[int]) -> List[int]:

    total = 1
    pre = []
    for i in nums:
        pre.append(total)
        total *= i

    # [1, 1, 2, 8]

    total = 1
    for i in range(len(nums)-1, -1, -1):
        pre[i] = pre[i] * total
        total = total * nums[i]

    return pre

assert productExceptSelf(nums) == [48,24,12,8]

