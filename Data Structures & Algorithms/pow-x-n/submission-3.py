class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            res = x
            for i in range(n-1):
                res *= x
            return res
        elif n < 0:
            res = x
            for i in range(abs(n)+1):
                res = res / x
            return res
        else:
            return 1