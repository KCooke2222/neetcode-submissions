class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # O(n)
        # O(1)
        # do diagonals adding to res, single count overlap

        res = 0
        for i in range(len(mat)):
            p = (i, i)
            s = (len(mat) - i - 1, i)
            if p == s:
                res += mat[p[0]][p[1]]
            else:
                res += mat[p[0]][p[1]]
                res += mat[s[0]][s[1]]


        return res