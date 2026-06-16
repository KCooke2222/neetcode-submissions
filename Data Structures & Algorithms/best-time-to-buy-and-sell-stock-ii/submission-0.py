class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n)
        # summation of all positive differences in stock price
        # iterate and compare cur to cur + 1 if pos add to res

        res = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                res += prices[i+1] - prices[i]

        return res
