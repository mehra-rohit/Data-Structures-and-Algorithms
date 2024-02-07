# coins = [1, 5, 10]
# amount = 20
# In how many ways you can provide change using the coins provided for the amount
# We have to count the number of ways and repeat item selection is allowed : Unbounded Knapsack, count type


def coin_change(coins: list[int], amount: int, n: int):

    # initialise dp table
    t = [[-1 for i in range(amount+1)] for j in range(n+1)]

    # base conditions
    for i in range(amount+1):
        t[0][i] = 0
    for i in range(n+1):
        t[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, amount+1):
            if coins[i-1] <= j:
                t[i][j] = t[i][j-coins[i-1]] + t[i-1][j]
            elif coins[i-1] >j:
                t[i][j] = t[i-1][j]
    return t[n][amount]


coins = [1, 2, 3]
amount = 3
assert coin_change(coins, amount, len(coins)) == 3


