def count_zeros(n,count=0):
    print(n,count)
    if n%10==n:
        return count
    elif n%10==0:
        count +=1
        return count_zeros(n//10,count)
    else:
        return count_zeros(n//10,count)


print(count_zeros(1001))
