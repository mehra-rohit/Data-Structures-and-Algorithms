class Solution(object):
    def swap_element(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
        return arr
    
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return -1

        i = 0
        while i < len(nums):
            if nums[i]<len(nums) and nums[i]!=i:
                self.swap_element(nums, nums[i],i)
            else: 
                i += 1
        
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)
