def RBS(arr,target,s,e):
    #base case
    if s>e:
        return -1

    m = (s+e)//2
    if arr[m]==target:
        return m
    elif arr[s]<=arr[m]:
        if arr[s]<=target and arr[m]>=target:
            return RBS(arr,target,s,m-1)
        else :
            return RBS(arr,target,m+1,e)
    elif arr[m]>=target and arr[e]>=target:
        return RBS(arr,target,m+1,e)
    else : 
        return RBS(arr,target,s,m-1)
arr = [5,6,7,8,9,1,2,3,4]
print(RBS(arr,5,0,len(arr)-1))
