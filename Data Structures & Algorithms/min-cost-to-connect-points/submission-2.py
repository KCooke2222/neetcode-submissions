class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # O(ElogE)
        # O(E)
        # create adj list with weighted edges
        # prim's alg
            # if len(visit) = len(points), done
            # add nodes neighbors to minheap
            # take smallest from minheap not in visit
                # add to cost, mark visit, and continue


        adj = {i: [] for i in range(len(points))}
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i == j: 
                    continue

                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                adj[i].append((dist, j))


        res = 0
        visit = set([0])
        minheap = []
        def prims(node):
            nonlocal res

            if len(visit) == len(points): 
                return

            for neigh in adj[node]:
                heapq.heappush(minheap, neigh)

            while minheap[0][1] in visit: 
                heapq.heappop(minheap)

            dist, nextNode = heapq.heappop(minheap)

            res += dist
            visit.add(nextNode)
            prims(nextNode)



        prims(0)
        return res

