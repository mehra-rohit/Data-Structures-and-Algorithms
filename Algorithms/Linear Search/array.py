# Search an element in an array
# Best case - O(1) : if target is the first element in array then it doesnot matter if array size is big or small.
# Worst Case = O(N) : if target is the last element, we will have to go through entire array

def linear_search_in_array(arr, target):

  if len(arr)==0:
    print(f'{target} not present in array'
    return -1

  for index, val in enumerate(arr):
    if val == target:
      print(f'{target} found in array at index {index}')
      return index

  print(f'{target} not present in array'
  return -1
