# given string s = 'agbcba'
# find largest palindromic subsequence
# lps(s) = lcs(s, reversed(s))


def longestPalindromeSubseq(s):
    """
    :type s: str
    :rtype: int
    """

    y = s[::-1]

    n = len(s)
    m = len(y)

    t = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    # initialisation
    for i in range(m + 1):
        t[0][i] = 0
    for i in range(n + 1):
        t[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == y[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    return t[n][m]


s = 'agbcba'
assert longestPalindromeSubseq(s) == 5
