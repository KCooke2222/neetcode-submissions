class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstra with min heap
        n = len(grid)
        cost = [[float("inf") for i in range(n)] for i in range(n)]
        visited = [[0 for i in range(n)] for i in range(n)]

        
        heap = []
        def dijkstra(i, j):
            if (i, j) == (n-1, n-1):
                return cost[i][j]

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for r, c in directions:
                nr, nc = i + r, j + c
                if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                    cost[nr][nc] = max(cost[i][j], grid[nr][nc])
                    heapq.heappush(heap, (cost[nr][nc], (nr,nc)))
                    visited[nr][nc] = 1
            

            ni, nj = heapq.heappop(heap)[1]
            return dijkstra(ni, nj) 

        
        cost[0][0] = grid[0][0]
        return dijkstra(0, 0)
