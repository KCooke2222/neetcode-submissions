class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # dfs
        # check all sides if empty or 0
            # add to perimeter count

        perimeter = 0
        visit = set()

        def dfs(i, j):
            nonlocal perimeter
            if (i, j) in visit:
                return
            
            visit.add((i, j))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for r, c in directions:
                nr = i + r
                nc = j + c

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == 0:
                        perimeter += 1
                    else:
                        dfs(nr, nc)
                else:
                    perimeter += 1


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter