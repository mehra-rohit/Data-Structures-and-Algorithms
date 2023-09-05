# find alphabet in string

def linear_search_string(string, target):
  if len(string)==0:
    return -1
  for index, val in enumerate(string):
    if val == target:
      return index
  return -1
