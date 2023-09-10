class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        temp = {}

        for i in range(len(nums)):
            if nums[i] in temp:
                return True
            else: 
                temp[nums[i]]=i
        
        return False
