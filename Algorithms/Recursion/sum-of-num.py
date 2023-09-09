
def sum_func(n):
    if n==0:
        return 0
    else: 
        return n%10 + sum_func(n//10)
print(sum_func(123))
