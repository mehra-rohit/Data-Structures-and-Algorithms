'''
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
'''

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


board2 = [["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:

    # row check
    for i in range(9):
        temp = set()
        for j in range(9):
            if board[i][j] != "." and board[i][j] in temp:
                return False
            temp.add(board[i][j])

    # column check
    for i in range(9):
        temp = set()
        for j in range(9):
            if board[j][i] != "." and board[j][i] in temp:
                return False
            temp.add(board[j][i])

    
    # cube check
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = set()
            for k in range(0, 3):
                for l in range(0,3):
                    if board[i+k][j+l] != "." and board[i+k][j+l] in temp:
                        return False
                    temp.add(board[i+k][j+l])
    return True


assert isValidSudoku(board) == True
assert isValidSudoku(board2) == False

from collections import defaultdict

# time -> O(9*9), space -> O(9)
def isValidSudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    box = defaultdict(set)

    for r in range(len(board)):
        for c in range(len(board)):

            if board[r][c] == ".":
                continue

            # check if value is in rows, cols, box and return False
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in box[(r//3, c//3)]:
                return False

            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            box[(r//3, c//3)].add(board[r][c])

    return True

assert isValidSudoku(board) == True
assert isValidSudoku(board2) == False
