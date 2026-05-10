class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval

        for interval in intervals:
            # push left intervals
            if interval[1] < start:
                res.append(interval)
            
            # push right intervals
            elif interval[0] > end:
                res.append([start, end])
                res.extend(intervals[intervals.index(interval):])
                return res

            # merge
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])

        res.append([start, end])
        return res
