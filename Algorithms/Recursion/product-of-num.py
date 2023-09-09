def product_func(n):
    if n==0:
        return 1
    else: 
        return (n%10)*product_func(n//10)
