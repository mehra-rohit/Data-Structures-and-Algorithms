def max_element(arr,max_e,i=0):
    if i == len(arr):
        return max_e
    if arr[i]>arr[max_e]:
        max_e = i
    return max_element(arr,max_e,i+1)

def insert_sort(arr,i=0):
    #base condition
    if i==len(arr):
        return
    max_ele = max_element(arr[:len(arr)-i],0)
    #swap element
    temp = arr[max_ele]
    arr[max_ele]=arr[len(arr)-1-i]
    arr[len(arr)-1-i] = temp
    
    return insert_sort(arr,i+1)
    
arr = [1,4,5,2,4,6,7]

insert_sort(arr)
print(arr)
