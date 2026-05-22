class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # attempt to place queen on each pos
            # when placed remove valid positions from valid board (row, col, diag)
            # continue until 4 are placed then add to res and bactrack

        res = []
        path = [["."] * n for _ in range(n)]
        cols = set()
        posDiag = set()
        negDiag = set()

        def addRes(path):
            pathConversion = []
            for r in range(n):
                pathConversion.append("".join(path[r]))
            
            res.append(pathConversion)

        def dfs(r):
            if r == n:
                addRes(path)
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                    
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                path[r][c] = "Q"

                dfs(r+1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                path[r][c] = "."

        dfs(0)
        return res
                         
