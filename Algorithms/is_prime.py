# normal solution
def check_prime(n):
  if n=<1:
    return 'neither prime nor composite'
c = 2
while c < n:
  if n%c == 0:
    return f'{n} is not a prime number'
  c = c+1
return f'{n} is a prime number'

'''
1*12 = 12
2*6 = 12
3*4 = 12
4*3 = 12
6*2 = 12
12*1 = 12

so we just have to check for half of the cases, since other half is just the same.
'''
# optimised solution
def check_prime(n):
  if n=<1:
    return 'neither prime nor composite'
c = 2
while c**2 < n:
  if n%c == 0:
    return f'{n} is not a prime number'
  c = c+1
return f'{n} is a prime number'
