class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals
        # dp, memo (prev interval, index in intervals)
        # dfs
            # on each overlap remove either overlapping interval
            # otherwise dfs prev and i forward

        intervals.sort()

        memo = {}

        def dfs(prev, i):
            if i > len(intervals) - 1:
                return 0

            if (prev, i) in memo:
                return memo[(prev, i)]

            if intervals[i][0] < intervals[prev][1]:
                memo[(prev, i)] = 1 + min(dfs(prev, i + 1), dfs(i, i + 1))
            else:
                memo[(prev, i)] = dfs(i, i + 1)

            return memo[(prev, i)]

        
        return dfs(0, 1)