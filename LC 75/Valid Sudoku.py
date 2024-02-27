# Each row must contain 1-9 without repetition
# Each column must contain 1-9 without repetition
# Each subset of 3*3 must contain 1-9 without repetition

# Pseudo Algo
# 1,2 can be checked through iterating entire sudoku
# store each element in set or dict check for existence, "." pass
# 3 check needs boxwise iteration, iterate through board, within this iterate for 3*3 space and check
# update the iteration by 3


def valid_sudoku(board: list[list[str]]) -> bool:
    # first check

    for r in range(len(board)):
        temp = set()
        for c in range(len(board)):
            if board[r][c] in temp and board[r][c] != ".":
                return False
            else:
                temp.add(board[r][c])

    # second check
    for c in range(len(board)):
        temp = set()
        for r in range(len(board)):
            if board[r][c] in temp and board[r][c] != ".":
                return False
            else:
                temp.add(board[r][c])

    # third check
    for r in range(0, len(board), 3):
        for c in range(0, len(board), 3):
            temp = set()
            for rs in range(r, 3 + r):
                for cs in range(c, 3 + c):
                    if board[rs][cs] in temp and board[rs][cs] != ".":
                        return False
                    else:
                        temp.add(board[rs][cs])

    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board2 = [["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

assert valid_sudoku(board) == True
assert valid_sudoku(board2) == False

# Optimised version
from collections import defaultdict


def valid_sudoku_op(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxs = defaultdict(set)

    for r in range(len(board)):
        for c in range(len(board)):

            if board[r][c] == ".":
                continue

            if (board[r][c] in rows[r]
                  or board[r][c] in cols[c]
                  or board[r][c] in boxs[(r // 3, c // 3)]):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            boxs[(r // 3, c // 3)].add(board[r][c])


    return True


# assert valid_sudoku_op(board) == True
assert valid_sudoku_op(board2) == False

