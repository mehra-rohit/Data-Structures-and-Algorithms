class Solution(object):
    def swap_elements(self, nums, a, b):
        temp = nums[a]
        nums[a]=nums[b]
        nums[b]=temp
        return nums

    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        i = 0
        while i<len(nums):
            correct = nums[i]-1
            if nums[i]!=nums[correct]:
                self.swap_elements(nums,i,correct)
            else:
                i += 1
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans=[nums[i],i+1]
        return ans
        
