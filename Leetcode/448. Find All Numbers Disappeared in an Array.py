class Solution(object):
    def swap_element(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
        return arr
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return -1

        i = 0
        while i < len(nums):
            correct = nums[i]-1
            if nums[i]!=nums[correct]:
                self.swap_element(nums, i,correct)
            else: 
                i += 1
        ans = []
        for i in range(len(nums)):
            if i+1!=nums[i]:
                ans.append(i+1)
        return ans
