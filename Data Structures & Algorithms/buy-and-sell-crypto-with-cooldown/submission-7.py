class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp, dfs, memo on (price holding or none, day)
        # dfs
            # bounds, memo
            # if holding
                # sell: holding + dfs(None, day + 2)
                # wait: dfs(holding, day + 1)
            # else
                # buy: -price + dfs(holding, day + 1)
                # wait: dfs(holding, day + 1)

        memo = {}

        def dfs(holding, day):
            if day >= len(prices):
                return 0
            if (holding, day) in memo:
                return memo[(holding, day)]

            if holding:
                memo[(holding, day)] = max(prices[day] + dfs(False, day + 2), dfs(True, day + 1))
            else:
                memo[(holding, day)] = max(-prices[day] + dfs(True, day + 1), dfs(False, day + 1))

            return memo[(holding, day)]


        return dfs(False, 0)