"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
"""
# op solution : logn + logm
# do binary search to find the row in which the target exist
# do 2nd binary search in row to find target

def search_2D(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    top, bot = 0, rows - 1

    while top <= bot:
        mid = (top + bot) // 2
        # mid is our current row
        # if target is smaller than first element of the current row move bot
        if target < matrix[mid][0]:
            bot = mid - 1
        # if target is larger than last element of the current row move top
        elif target > matrix[mid][-1]:
            top = mid + 1
        else:
            break

    # check if looped break and not finish
    if top > bot:
        return False

    row = (top + bot) // 2
    l, r = 0, cols - 1
    while l <= r:
        mid = (l+r) //  2
        if target < matrix[row][mid]:
            r = mid - 1
        elif target > matrix[row][mid]:
            l = mid + 1
        else:
            return True
    return False


matrix1 = [[1, 3, 5, 7],
           [10, 11, 16, 20],
           [23, 30, 34, 60]]
target1 = 13

print(search_2D(matrix1, target1))
