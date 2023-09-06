#ceiling of a number
# given an arr with n values find the closest number in array arr which is greater than or equals to integer target 

def ceiling_of_num(arr, target):

  if len(arr)==0:
    return - 1 

  start = 0
  end = len(arr) - 1

  while start <= end:
    mid = (start+end)//2

    if arr[mid] == target:
      return f'target element {target} found at index {mid} in array'
    elif arr[mid] < target:
      end = mid - 1
    else:
      start = mid + 1
# if target is present in array binary search code will return it, otherwise when while loop will end start > end and start will be closest number which is greater than target
  return start

def floor_of_num(arr, target):

  if len(arr)==0:
    return - 1 

  start = 0
  end = len(arr) - 1

  while start <= end:
    mid = (start+end)//2

    if arr[mid] == target:
      return f'target element {target} found at index {mid} in array'
    elif arr[mid] < target:
      end = mid - 1
    else:
      start = mid + 1
# if target is present in array binary search code will return it, otherwise when while loop will end start > end and end will be closest number which is smaller than target
  return end
