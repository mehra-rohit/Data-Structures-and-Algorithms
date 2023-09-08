'''
Takes ith max/min element in the array and put it at its correct index.
In case of max at the end
In case of min at the beginning
Time complexity : worst (O(N^2))
'''

def max_arr(arr, start, end):
    max_val = 0
    for i in range(start,end):
        if arr[i]>arr[max_val]:
            max_val = i
    return max_val
    
def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr
    
def selection_sort(arr):
    #max element method
    #find max, swap with last element, iterate over array

    for i in range(len(arr)):
        max_element = max_arr(arr, 0, len(arr)-i)
        swap(arr, max_element, len(arr)-i-1)

    return arr

print(selection_sort([1,5,4,3,2]))
print(selection_sort([11,5,45,3,23]))
