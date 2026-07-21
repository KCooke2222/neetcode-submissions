class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # store rows / cols to 0 in first row and col
        # store if we will set first col in seperate var (first row in 0,0)
        # iterate over the matrix to store what r/c to 0
        # 0 the r/c

        firstCol = False
        firstRow = False

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if c == 0:
                        firstCol = True
                    if r == 0: 
                        firstRow = True
                    
                    matrix[0][c] = 0
                    matrix[r][0] = 0


        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0

        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0

        if firstRow:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0


        if firstCol:
            for r in range(len(matrix)):
                matrix[r][0] = 0

        