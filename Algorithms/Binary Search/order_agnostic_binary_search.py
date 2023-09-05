#when we dont know if array is sorted in ascending order or descending order

def order_agnostic_binary_search(arr,target):

  start = 0
  end = len(arr)-1

  is_asc = True
  if arr[start]> arr[end]:
    is_asc = False

  while start <= end:
    mid = (start + end)//2
    if arr[mid]==target:
      return mid,arr
    elif arr[mid]<target:
      if is_asc == True:
        start = mid + 1
      else: end = mid-1
    else :
      if is_asc == True:
        end = mid-1
      else: start = mid + 1
