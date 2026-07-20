class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        # maintain res
        # prev, cur
        # iterate over intervals
            # if overlap, prev = merge
            # else, append prev, new prev

        res = []
        intervals.sort()

        prev = None
        for cur in intervals:
            if not prev: 
                prev = cur
                continue

            if cur[0] <= prev[1]:
                prev = [min(prev[0], cur[0]), max(cur[1], prev[1])]
            else:
                res.append(prev)
                prev = cur

        res.append(prev)
        return res

