# given two string X = 'heap' and Y = 'pea'
# Find minimum number of insertion and deletion required to convert X into Y
# X: (not common with Y + common with Y), Y: (not common with X + common with X)
# X can be converted into Y by inserting (not common with X) and deleting (not common with Y)
# insertion = len(Y)-common(X,Y) and deletion = len(X) - common(X,Y)
# we can find common(X,Y) subsequence by largest common subsequence algorithm


# Top-Down Approach
def lcs(x: str, y: str, n: int, m: int) -> int:
    # DP table
    t = [[-1 for i in range(m+1)] for j in range(n+1)]
    # initialisation
    for i in range(n+1):
        t[i][0] = 0
    for j in range(m+1):
        t[0][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[n][m]


def min_iteration_convert(x: str, y: str):
    n = len(x)
    m = len(y)
    common_length = lcs(x, y, n, m)
    insert_count = m - common_length
    del_count = n - common_length
    return (insert_count, del_count)


X = 'heap'
Y = 'pea'
assert min_iteration_convert(X, Y) == (1,2)

