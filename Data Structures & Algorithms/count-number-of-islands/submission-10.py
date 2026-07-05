class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(n*m)
        # start bfs at each position
            # flip all 1s we can reach to 0s
        # count number of bfs with > 0 1s

        def bfs(r, c):
            if grid[r][c] == "0":
                return False

            visit = set()
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            

            while q:
                cr, cc = q.popleft()
                grid[cr][cc] = "0"

                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc

                    if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])) or grid[nr][nc] == "0" or (nr, nc) in visit:
                        continue

                    q.append((nr, nc))
                    visit.add((nr, nc))

            return True


        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if bfs(r, c):
                    res += 1

        return res