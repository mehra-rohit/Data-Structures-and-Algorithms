# Simple approach
def compute_power(x,n):
  '''
  x : base number whose power needs to be computed (int)
  n : power (int)
  '''
  result = 1
  for i in range(0,n):     # if n is 0 this not get triggered and 1 will be returned.
    result = result*i
  return result
# Time complexity : O(n)
# Space complexity : O(1)

# Recursive Way
def cp(x,n):
    if n==0:
        return 1
    else:
        return x*cp(x,n-1)

# PSEUDO CODE FOR OPTIMIZED SOLUTION
'''
- If n is even: 
    temp*temp
    where temp = power(x,n/2)
- If n is odd:
    power(x,n-1)*x. # if n is odd n-1 will always be even and we just have to compute is one more time only
'''

#Python Implementation

def compute_power(x,n):
    if n == 0:
        return 1
    temp = power(x,n//2)
    temp = temp * temp
    if n%2==0:
        return 1
    else:
        return temp*x
# Time complexity : O(logn)
# Space complexity : O(1)
