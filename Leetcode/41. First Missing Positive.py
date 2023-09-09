class Solution(object):
    def swap_element(self, nums, a, b):

        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

        return nums

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            if nums[0]==1:
                return 2
            else:
                return 1
        i = 0
        while i < len(nums):
            correct = nums[i]-1
            if nums[i]<len(nums) and nums[i]>=0 and nums[i]!=nums[correct]:
                self.swap_element(nums,i,correct)
            else:
                i = i+1
        
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return i+1
        return nums[len(nums)-1]+1
