class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # dijkstras but with max instead of summation of weights

        minheap = [(0, 0, 0)]
        visit = set()
        target = (len(heights) - 1, len(heights[0]) - 1)

        while minheap:
            cost, r, c = heapq.heappop(minheap)

            if (r, c) in visit:
                continue
            
            if (r, c) == target:
                return cost

            visit.add((r, c))

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]):
                    nCost = max(cost, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(minheap, (nCost, nr, nc))

        


            

            

            