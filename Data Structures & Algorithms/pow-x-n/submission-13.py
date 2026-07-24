class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n < 0
        n = abs(n)

        if x == 0: return 0

        def dfs(x, n):
            if n == 0:
                return 1


            remainder = x if n % 2 else 1
            split = dfs(x, n // 2)
            return split * split * remainder

        res = dfs(x, n)
        return 1/res if negative else res