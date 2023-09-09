#merge two sorted arrays
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
    
    print(i,j)
    return arr3+arr1[i:]+arr2[j:]
    
arr1 = [1,3,5]
arr2 = [2,4,6]
print(merge(arr1, arr2))
