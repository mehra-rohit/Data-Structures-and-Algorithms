def fibonacci(n):
  #base condition
  if n<2:
    return n
  #what our calls should return
  return fibonacci(n-1) + fibonacci(n-2)
