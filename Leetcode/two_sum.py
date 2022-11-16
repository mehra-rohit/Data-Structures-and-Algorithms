# Optimized Approach
def two_sum(nums, target):
    temp_dict = {}
    for i,num in enumerate(nums):
        rem = target-num:
        if rem in temp_dict:
            return [i,temp_dict[rem]]
        temp_dict[num]=i
        
time complexity : O(n)
    
    
# Simple Approach
def two_sum(nums, target):
    for i,num in enumerate(nums):
        for i2,num2 in enumerate(nums[i+1:]):
            if num+num2 == target:
                return [i,i2]
            
time complexity : O(n2)
