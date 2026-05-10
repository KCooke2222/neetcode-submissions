class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])

        res = []
        for q in queries:
            lengths = []
            heapq.heapify(lengths)
            i = 0

            # Collect intervals
            while i < len(intervals) and intervals[i][0] <= q:
                if intervals[i][1] >= q:
                    length = intervals[i][1] - intervals[i][0] + 1
                    heapq.heappush(lengths, length)
                i += 1

            if len(lengths):
                res.append(lengths[0])
            else:
                res.append(-1)

        return res