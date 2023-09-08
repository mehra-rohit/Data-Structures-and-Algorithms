# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        ans = -1
        if mountain_arr.length==0:
            return ans
        peak = self.peak_of_mountain(arr = mountain_arr)
        left_side = self.order_agnostic_binary_search(arr=mountain_arr,target = target, start = 0, end = peak)
        if left_side==-1:
            right_side = self.order_agnostic_binary_search(arr=mountain_arr,target = target, start = peak+1, end = mountain_arr.length() -1)
            ans = right_side
        else:
            ans = left_side
        
        return ans

    
    def order_agnostic_binary_search(self,arr,target, start, end):

        if arr.get(start)<arr.get(end):
            asc = True
        else :
            asc = False
        ans = -1

        while start<=end:
            mid = (start+end)//2
            if arr.get(mid)==target:
                return mid
            elif arr.get(mid)<target:
                if asc:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if asc:
                    end = mid-1
                else:
                    start = mid+1
        return ans

    def peak_of_mountain(self,arr):
        start = 0
        end = arr.length()-1

        while start<end:
            mid = (start+end)//2
            if arr.get(mid)>arr.get(mid+1):
                end = mid
            else:
                start = mid+1
        return start
