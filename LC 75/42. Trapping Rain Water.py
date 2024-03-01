# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
# [0,1,0,2,1,0,1,3,2,1,2,1]

# water storage capacity at index i will be
# min(l, r) - h[i], l -> max left height, r -> max right height

# O(n) + O(n) solution
# compute max_left for each position
# compute max_right for each position
# compute min(l,r)
# compute water capacity for each position and sum up


def rain_water(height: list[int]) -> int:
    # if height array is empty
    if not height:
        return 0
    max_left, max_right, temp = [], [], 0
    cap = 0
    # compute max_left
    for i in range(len(height)):
        temp = max(temp, height[i])
        max_left.append(temp)
    # compute max_right
    temp = 0
    for i in range(len(height) - 1, -1, -1):
        temp = max(temp, height[i])
        max_right.append(temp)
    # compute min_height
    for i in range(len(height)):
        min_height = min(max_left[i], max_right[len(height) - 1 - i])
        cap += max(0, min_height - height[i])
    return cap


height1 = []
print(rain_water(height1))
height2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rain_water(height2))


# using two pointer O(n) + O(1) memory
# take l,r as extreme values
# start from 1st index as extreme index cannot hold any water
# compute min(l,r) - height[i] -> this will be the water holding capacity at index i
# index i will be next to the pointer which we will be moving so update in an array
def rain_water_op(height: list[int]) -> int:
    if not height:
        return 0

    ans = 0
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            ans += max(0, leftMax - height[l])
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            ans += max(0,rightMax - height[r])


    return ans


height2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rain_water_op(height2))