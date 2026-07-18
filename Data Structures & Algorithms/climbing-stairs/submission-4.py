class Solution:
    def climbStairs(self, n: int) -> int:
        # backtrack
        # iterate from back
        # i = (i + 1) + (i + 2)
        # include bases

        steps = [0] * (n + 1)

        for i in range(n, -1, -1):
            if i == n:
                steps[i] = 1
            elif i == n - 1:
                steps[i] = 1
            else:
                steps[i] = steps[i + 1] + steps[i + 2]
            

        return steps[0]

        