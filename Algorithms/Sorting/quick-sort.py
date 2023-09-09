#quick sort
def swap(arr,a,b):
    temp = arr[a]
    arr[a]= arr[b]
    arr[b]= temp
    return

def quick_sort(arr,low,hi):
    
    if low>=hi:
        return
    s = low
    e = hi
    p = (s+e)//2
    
    while(s<=e):
        while(arr[s]<arr[p]):
            s += 1
        while(arr[e]>arr[p]):
            e -= 1
        if s<=e:
            swap(arr,s,e)
            s += 1
            e -= 1
    
    quick_sort(arr,low,e)
    quick_sort(arr,s,hi)
    
arr = [1,2,3,4,5,6,7,3,1,3,4]
quick_sort(arr,0,len(arr)-1)
print(arr)
