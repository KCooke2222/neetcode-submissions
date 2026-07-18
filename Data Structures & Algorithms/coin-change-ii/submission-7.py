class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp, memo on (pos in coins, amount left)
        # dfs
            # bounds, memo
            # take coin or not
            # return dfs(i, amount - coin) + dfs(i + 1, amount)

        memo = {}

        def dfs(i, a):
            if a == 0:
                return 1
            elif a < 0 or i >= len(coins):
                return 0

            if (i, a) in memo:
                return memo[(i, a)]

            memo[(i, a)] = dfs(i, a - coins[i]) + dfs(i + 1, a)
            return memo[(i, a)]

        return dfs(0, amount)