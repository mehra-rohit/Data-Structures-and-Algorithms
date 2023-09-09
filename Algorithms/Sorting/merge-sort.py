#merge sort with array copy pass
def merge(arr1,arr2):
    i=0
    j=0
    k=0
    arr3 = []
    
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i = i + 1
        else:
            arr3.append(arr2[j])
            j = j + 1
        k = k + 1

    return arr3+arr1[i:]+arr2[j:]
    
def merge_sort(arr):
    if len(arr)==1:
        return arr
        
    mid = len(arr)//2
    
    left = merge_sort(arr[:mid].copy())
    right = merge_sort(arr[mid:].copy())
    
    return merge(left, right)
    
arr = [1,3,5,2,8,7,6,4,2,3,4,5]
print(merge_sort(arr))


