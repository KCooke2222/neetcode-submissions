class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp with memo on index on t1 and t2
        # dfs(i, j)
            # bounds, memo
            # matching -> return 1 + dfs(i + 1, j + 1)
            # not match -> search match j + 1 or remove i + 1

        memo = {}

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            if text1[i] == text2[j]:
                res = max(res, 1 + dfs(i + 1, j + 1))
            else:
                res = max(res, dfs(i, j + 1))
                res = max(res, dfs(i + 1, j))

            memo[(i, j)] = res
            return res

        return dfs(0, 0)
