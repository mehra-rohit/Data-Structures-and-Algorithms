#print n factorial

def fact(n):
  #base case
  # when n is 1 return 1
    if n == 1:
      return 1
  return n*fact(n-1)
