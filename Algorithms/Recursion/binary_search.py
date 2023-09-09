# Binary Search Using Recursion
'''
Relation : F(n) = O(1) {comparison check} + F(n/2)
Base condition : 
termination condition = s>e
if mid==target : return mid
elif : mid <target:
	start = mid + 1
else : (mid > target)
	end = mid - 1
'''

def binary_search(nums, target, s, e):

	if s>e:
		return -1 # value not found
	mid = (s + e)//2
	if nums[mid]==target:
		return mid
	elif nums[mid]< target:
		s = mid+1
		return binary_search(nums, target, s, e)
	else:
		e = mid - 1
		return binary_search(nums,target,s,e)

nums = [1,3,4,5,7,10,12,55,100]
target = 12
s = 0
e = len(nums)-1
print(binary_search(nums, target, s, e))
