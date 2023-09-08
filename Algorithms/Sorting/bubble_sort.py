'''
Iterates through the array and checks if adjacent element is larger, if not swap.
By the end of first iteration largest value is at last index.
'''
def bubble_sort(arr):
    if len(arr)==0:
        return -1

    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
          #checking till second last index only as comparison is between j and j+1, if we do till last j+1 will give error
          if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            #update swap counter so loop continue
            swap = True
    
        if swap == False:
            break
    return arr
        
        
