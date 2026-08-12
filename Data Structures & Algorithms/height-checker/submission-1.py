class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # sort arr
        # compare each index

        counts = [0] * 101

        for h in heights:
            counts[h] += 1

        expected = []
        for num, count in enumerate(counts):
            for i in range(count):
                expected.append(num)


        res = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                res += 1

        return res