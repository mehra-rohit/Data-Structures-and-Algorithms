# Element position in infinite array
def binary_search(arr, target, start, end):
  ans = -1
  while start <= end:
    mid = (start+end)//2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      start = mid +1
    else : 
      end = mid - 1
  return ans

def pos_infinite_array(arr, target):

  start = 0
  end = 1

  while end < target:
    temp = start
    start = end
    end = end + 2*(end-temp + 1)
    
  ans = binary_search(arr,target, start, end)

  
