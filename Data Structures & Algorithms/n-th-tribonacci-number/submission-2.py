class Solution:
    def __init__(self):
        self.visit = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        if n in self.visit:
            return self.visit[n]

        res = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.visit[n] = res
        return res