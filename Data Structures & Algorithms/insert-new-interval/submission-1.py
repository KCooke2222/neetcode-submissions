class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        # push left intervals
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # merge overlap
        start, end = newInterval[0], newInterval[1]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            start, end = min(start, intervals[i][0]), max(end, intervals[i][1])
            i += 1

        merged = [start, end]

        # push merge
        res.append(merged)

        # push rest
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res
