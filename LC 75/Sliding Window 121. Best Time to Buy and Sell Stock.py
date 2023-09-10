class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        l = 0
        r = 1

        while r<len(prices):
            diff = prices[r]-prices[l]
            if diff>0:
                if diff > max_profit:
                    max_profit = diff
            else :
                l = r
            r += 1

        return max_profit
