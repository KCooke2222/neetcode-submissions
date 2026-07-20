class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort intervals
        # sort queries mainting (q, index)
        # create res of size index
        # tracking active intervals (minheap on (end, len)), iterating over queries
            # push intervals starting from nextInterval where start <= query to minheap
            # pop intervals with end < query
            # res[i] = min length of intervals in heap


        intervals.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])
        res = [0] * len(queries)

        minHeap = []
        i = 0
        for query, index in queries:
            while i < len(intervals) and intervals[i][0] <= query:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap, (intervals[i][1], length))
                i += 1

            while minHeap and minHeap[0][0] < query:
                heapq.heappop(minHeap)

            res[index] = min([l for e, l in minHeap]) if minHeap else -1


        return res