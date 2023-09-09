def bubble(arr, r, c):
    #base end case
    if r == 0:
        return
    
    if c<r:
        if arr[c]>arr[c+1]:
            temp = arr[c]
            arr[c] = arr[c+1]
            arr[c+1] = temp
        bubble(arr,r,c+1)
    else:
        bubble(arr,r-1,0)

arr = [1,4,5,2,4,6,7]
r = len(arr)-1
c = 0
bubble(arr, r, c)
print(arr)
