class Solution(object):
    def binary_search(self, arr, target, find_start_ind):
        
        ans = -1
        start = 0
        end = len(arr) - 1

        if len(arr)==0:
            return ans
        
        while start <= end:
            mid = (start + end)//2
            if arr[mid] == target:
                ans = mid
                if find_start_ind == True:
                    end = mid - 1
                else:
                    start = mid + 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return ans

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [-1,-1]

        start = self.binary_search(arr = nums, target = target, find_start_ind = True)
        if start!=-1:
            end = self.binary_search(arr = nums, target = target, find_start_ind = False)
            ans = [start,end]
        
        return ans

 
        
