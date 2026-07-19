class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp, memo on positions in (s1, s2, s3)
        # len s1 and s2 == len s3
        # dfs
            # base: neither s1 or s2 matches s3 => False
                # s3 reaches end => True
            # take paths where s1 or s2 == s3

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def dfs(i, j, k):
            if k == len(s3):
                return True

            if (i, j, k) in memo:
                return memo[(i, j, k)]

            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = res or dfs(i + 1, j, k + 1)
            
            if j < len(s2) and s2[j] == s3[k]:
                res = res or dfs(i, j + 1, k + 1)

            memo[(i, j, k)] = res
            return res

        return dfs(0, 0, 0)