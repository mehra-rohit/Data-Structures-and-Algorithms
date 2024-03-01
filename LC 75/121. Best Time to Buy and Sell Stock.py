"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""
"""
Sliding Window Solution
1. Iterate over the prices
2. Check for condition and update R and L pointers
    if curr_profit > 0
    -> maximum profit -> max(R - L, max_profit)
    curr_profit < 0
     L min(L, R)
     
var needed: left pointer, curr_profit
max_profit

Note: It is a maximisation problem so we need to initial max_profit as minimum val possible 0
    
"""


def max_profit_func(nums):
    L, curr_profit = 0, 0
    max_profit = 0

    for R in range(len(nums)):
        curr_profit = nums[R] - nums[L]
        if curr_profit > 0:
            max_profit = max(max_profit, curr_profit)
        else:
            if nums[R] < nums[L]:
                L = R
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
Output: 5

print(max_profit(prices))
