class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # sort arr
        # compare each index

        expected = sorted(heights)

        res = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                res += 1

        return res