class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = []
        temp = 1

        #this will store all pre num product at ith index of ans
        for i in nums:
            ans.append(temp)
            temp = temp*i
        
        temp = 1

        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i]*temp
            temp = temp*nums[i]
        
        return ans
