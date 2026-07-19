class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp, memo on pos in (w1, w2)
        # dfs
            # base: if either word finishes return remainder of other (insert / del)
            # if c1 == c2, increment both words
            # else:
                # insert: +1, inc w2
                # del: +1, inc w1
                # replace: +1, inc both

        memo = {}

        def dfs(i, j):
            if i >= len(word1):
                return len(word2) - j

            if j >= len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))

            return memo[(i, j)]


        return dfs(0, 0)