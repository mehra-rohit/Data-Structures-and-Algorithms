
'''
fibonacci numbers is a series of numbers : 1,1,2,3,,5,8........
f(n) = f(n-1) + f(n-2)
f(0) = 1
f(1) = 1
'''

# Naive Solution using Recursion

def fibonacci(n):
    #base condition
    if n <=1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))

# fibonacci(50) not able to compute, timeout

# Optimised solution
def fib(n):
    fib = [0]*(n+1)
    fib[0] = 1
    fib[1] = 1

    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]

print(fib(50))

