class Solution:
    def climbStairs(self, n: int) -> int:
        # dfs memo
        # count of paths: i = (i + 1) + (i + 2)
        # out of bounds: return 0
        # end: return 1

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            if i > n:
                return 0

            memo[i] = dfs(i + 1) + dfs(i + 2)

            return memo[i]

        return dfs(0)