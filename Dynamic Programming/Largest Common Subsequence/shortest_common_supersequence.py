# X = 'aggtab'
# Y = 'GXTXAYB'
# we have to find the length of shortest common super-sequence
# X : (not common + common), Y : (not common + common)
# shortest common supersequence = X(not common) + Y(not common) + common(X or Y) : len(X) + len(Y) - len(common(X,Y))
# Therefore we just have to find the length of largest common sequence here.


# Top Down Approach
def largest_common_sequence(x: str, y: str, n: int, m: int) -> int:
    # DP table
    t = [[-1 for i in range(m+1)] for j in range(n+1)]
    # base case initialisation
    for i in range(n+1):
        t[i][0] = 0
    for i in range(m+1):
        t[0][i] = 0
    # run iteration after base condition initialisation
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    return t[n][m]


def shortest_common_supersequence(x: str, y: str):
    n = len(x)
    m = len(y)

    return n + m - largest_common_sequence(x,y,n,m)


X = 'aggtab'
Y = 'gxtxayb'
assert shortest_common_supersequence(X, Y) == 9

