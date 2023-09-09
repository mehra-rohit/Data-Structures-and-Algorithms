def linear_search(arr,target, i = 0):
    
    #base condition
    if arr[i]==target:
        return i
    elif i==len(arr)-1:
        return 'Not Found'
    else:
        #recursive loop 
        return linear_search(arr,target,i+1)

    
print(linear_search([1,2,3,1,1,2,3],10))

#multiple occurences
def linear_search(arr,target, i = 0,ind = []):
    
    #base condition
    if i<len(arr):
        if arr[i]==target:
            ind.append(i)
        return linear_search(arr,target,i+1,ind)
    else:
        return ind
    
print(linear_search([1,2,3,10,10,2,3,10],10))
