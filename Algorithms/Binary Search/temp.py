# Binary Search Implementation

def binaray_search(arr, target):

  start = 0
  end = len(arr) - 1
  
  while start <= end:
    mid = (start + end)//2
    if arr[mid]==target:
      return mid,arr
    elif arr[mid]<target:
      start = mid + 1
    else :
      end = mid-1
      
  return f'{target} not present in array'
