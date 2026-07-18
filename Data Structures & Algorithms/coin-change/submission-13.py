class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp
        # memo min coins to make any amount
            # dfs try all coins each step

        memo = [None] * (amount + 1)

        def dfs(a):
            if a == 0:
                return 0
            if memo[a] != None:
                return memo[a]

            res = -1
            for c in coins:
                if a - c >= 0:
                    path = dfs(a - c)
                    if path == -1:
                        continue

                    if res == -1:
                        res = path
                    else:
                        res = min(res, path) 

            memo[a] = res + 1 if res != -1 else -1

            return memo[a]

        return dfs(amount)
            