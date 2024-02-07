# Find the length of largest common subsequence between two give strings.
# X : 'abcdgh', Y : 'abedfha'

# Recursive Solution
# 1. Base Condition : Whenever any string length passed to function is zero, return 0
# 2. Input -> Small (every next function call should be with smaller input)
# 3. Choice Diagram :
# a. Match is found : we subtract length 1 from both X, Y and pass to function again.
# b. Match is not found :
# b1. Subtract length 1 from X, pass Y as it is
# b2. Pass X as it is, subtract length 1 from Y
# We do max(b1,b2) since we are interested in the largest sequence.

def lcs(x: str, y: str, n: int, m: int):
    # base condition
    if n == 0 or m == 0:
        return 0
    # choice diagram code
    if x[n-1] == y[m-1]:
        return 1 + lcs(x, y, n-1, m-1)
    else:
        return max(lcs(x, y, n-1, m), lcs(x, y, n, m-1))


X = 'abcdgh'
Y = 'abedfha'

assert lcs(X, Y, len(X), len(Y)) == 4


# Recursive + Memoized Solution

def lcs(x: str, y: str, n: int, m: int):
    if n == 0 or m == 0:
        return 0

    if t[n][m] != -1:
        return t[n][m]

    if x[n-1] == y[m-1]:
        t[n][m] = 1 + lcs(x, y, n-1, m-1)
    else:
        t[n][m] = max(lcs(x, y, n-1, m), lcs(x, y, n, m-1))

    return t[n][m]


X = 'abcdgh'
Y = 'abedfha'

t = [[-1 for i in range(len(Y)+1)] for j in range(len(X)+1)]
lcs(X, Y, len(X), len(Y))
assert t[len(X)][len(Y)] == 4


# Top Down Solution

def lcs(x: str, y: str, n: int, m: int):
    # initialise dp table
    t = [[-1 for i in range(m+1)] for j in range(n+1)]

    for i in range(m+1):
        t[0][i] = 0
    for i in range(n+1):
        t[i][0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])

    return t[n][m]


X = 'abcdgh'
Y = 'abedfha'
assert lcs(X, Y, len(X), len(Y)) == 4


# print the subsequence
def lcs_print(x: str, y: str, n: int, m: int) -> str:
    t = [[-1 for i in range(m+1)] for j in range(n+1)]

    # initialisation
    for i in range(n+1):
        t[i][0] = ''
    for j in range(m+1):
        t[0][j] = ''

    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                t[i][j] = x[i-1] + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    ans = ''
    for i in t[n][m]:
       ans = i + ans
    return ans


X = 'abcdgh'
Y = 'abedfha'
assert lcs_print(X, Y, len(X), len(Y)) == 'abdh'

