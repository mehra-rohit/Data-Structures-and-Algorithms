import math

def rev(n):
    if n%10==n:
        return n
    else : 
        return (n%10)*pow(10,(math.floor(math.log(n,10)))) + rev(n//10)

#without log
def rev_n(n):
    if n==0:
        return
    else:
        sum_ = sum_*10 + n%10
        rev_frev_nunc(n//10)
    
sum_ = 0
print(rev(123))
print(rev(123))
