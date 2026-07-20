"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # most overlapping meetings at one time
        # sort intervals
        # iterate over intervals
            # place into minheap by endTime
            # pop off minheap based on cur start
            # update res = res or minheap size

        intervals.sort(key=lambda i: i.start)
        endTimes = []
        res = 0

        for interval in intervals:
            end = interval.end
            start = interval.start
    
            heapq.heappush(endTimes, end)
            
            while endTimes[0] <= start:
                heapq.heappop(endTimes)

            res = max(res, len(endTimes))


        return res