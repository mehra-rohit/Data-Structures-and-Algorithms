class Solution(object):
    def swap_elements(self,arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
        return arr

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)==0:
            return -1
        
        i = 0
        while i < len(nums):
            if nums[i]!=i+1:
                correct = nums[i]-1
                if nums[i]!=nums[correct]:
                    self.swap_elements(nums, i, correct)
                else: 
                    return nums[i]
            else:
                i += 1
