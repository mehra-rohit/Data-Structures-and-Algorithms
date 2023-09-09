def is_sorted(arr,i=0):
    
    if i==len(arr)-1:
        return True
    elif arr[i]>arr[i+1]:
        return False
    else:
        return is_sorted(arr,i+1)


print(is_sorted([1,2,8,3,4,5]))
    
