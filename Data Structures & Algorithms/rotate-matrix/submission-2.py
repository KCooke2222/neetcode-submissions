class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l): # diff r and l
                top, bottom = l, r

                # save topleft
                topLeft = matrix[top][l + i]

                # bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # bot right -> bot left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # top r -> bot r
                matrix[bottom][r - i] = matrix[top + i][r]

                # top l -> top r
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
