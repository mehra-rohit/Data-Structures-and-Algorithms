'''
loop 1 : iterate over all the elements in array
loop 2: puts the element at its right position
'''

def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr
    
def insertion_sort(arr):

    if len(arr)==0:
        return -1

    #loop 1 iterates over arr
    for i in range(1,len(arr)):
        #loop 2 checks if element + 1 < element, if so then swaps
        swap_ = False
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                swap(arr, j, j-1)
                swap_ = True
            if swap_ == False:
                break
    return arr

print(insertion_sort([1,5,4,3,2]))
print(insertion_sort([11,5,45,3,23]))
        

  
