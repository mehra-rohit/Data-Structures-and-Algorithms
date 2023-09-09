#when element are given from 1 to N, N element in a sorted array will have N-1 index.

def swap_element(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return temp

def cyclic_sort(arr):

    if len(arr)==0:
        return -1

    i = 0
    while i < len(arr)-1:
        correct = arr[i]-1
        if arr[correct] != arr[i]:
            swap_element(arr, i, correct)
        else: i += 1
    
    return arr

print(cyclic_sort([1,5,4,3,2]))
print(cyclic_sort([5,6,8,3,4,2,1,7]))
