def peak_of_mountatin(arr):
  ans = -1
  start = 0
  end = len(arr) - 1

  while start<=end:
    mid = (start + end)//2
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
      return mid
    elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
      start = mid +1
    elif arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]:
      end = end - 1

return ans

#optimised solution
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # ans = -1    
        start = 0
        end = len(arr) - 1

        while start<end:
            mid = (start + end)//2
            if arr[mid] > arr[mid+1] :
                end = mid
            else :
                start = mid + 1

        return start
        
