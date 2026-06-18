class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dfs with memo
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        memo = {}
        def dfs(r, c):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0

            if r == m - 1 and c == n - 1:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]

            
            
            res = dfs(r + 1, c) + dfs(r, c + 1)

            memo[(r, c)] = res
            return res

        return dfs(0, 0)
            

