#merge sort with array copy pass
def merge(arr,s,m,e):
    i=s
    j=m
    k=0
    arr3 = []
    while(i<m and j<=e):
        if arr[i]<arr[j]:
            arr3.append(arr[i])
            i = i + 1
        else:
            arr3.append(arr[j])
            j = j + 1
    arr3 = arr3 + arr[i:m] + arr[j:e+1]
    for l in range(len(arr3)):
        arr[s+l] = arr3[l]
    print(arr[s:e+1])
    return
    
def merge_sort(arr,s,e):
    if e-s ==1:
        return
        
    m = (s+e)//2

    merge_sort(arr,s,m)
    merge_sort(arr,m,e)
    
    return merge(arr,s,m,e)
    
arr = [1,2,3,4,5,6,7,3,1,3,4]
merge_sort(arr,0,len(arr)-1)
print(arr)
