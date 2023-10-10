# length = [1, 2, 3, 4, 5, 6, 7, 8]
# price = [1, 5, 8, 9, 10, 17, 17, 20]
# l = 8 (length of rod)

# We have to cut the rod in such a way that max profit is obtained, length array has all the valid rod cutting options
# price array has the corresponding prices.
# Also, there is no limitation on length selection, we can even cut rod of length 8, 8 times by length of 1.

# This is direct implementation of unbounded knapsack.

def rod_cutting(length: list[int], price: list[int], l: int, n: int):
    # initialise dp table
    t = [[-1 for i in range(l+1)] for j in range(n+1)]

    for i in range(l+1):
        t[0][i] = 0
    for i in range(n+1):
        t[i][0] = 0

    for i in range(1,n+1):
        for j in range(1,l+1):
            if length[i-1] <= j:
                t[i][j] = max(price[i-1] + t[i][j-length[i-1]], t[i-1][j])
            elif length[i-1] > j:
                t[i][j] = t[i-1][j]
    return t[n][l]


length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
l = 8
assert rod_cutting(length, price, l, len(length)) == 22
