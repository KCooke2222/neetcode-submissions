class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # O(n)
        # O(1)
        # do diagonals adding to res, single count overlap

        res, n = 0, len(mat)

        for r in range(n):
            res += mat[r][r]
            res += mat[r][n - r - 1]

        return res - (mat[n // 2][n // 2] if n & 1 else 0)