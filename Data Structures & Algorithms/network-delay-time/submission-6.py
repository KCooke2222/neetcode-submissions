class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # O(V * ElogE)
        # build adj list of edges with weights
        # init dist to each node as inf
        # visit set
        # starting from k
            # add neighbors to minheap
            # pop from minheap until smallest weight unvisited node
            # add this node to dist (curDist + weight)
            # continue processing nextNode until len(visit) == n
        # return max of dist.values()

        adj = defaultdict(list)
        for ui, vi, ti in times:
            adj[ui].append((ti, vi))

        dist = {}
        for i in range(1, n+1):
            dist[i] = float("inf")
        dist[k] = 0
        visit = set([k])

        node = k
        minheap = []
        while len(visit) < n:
            for d, nn in adj[node]:
                heapq.heappush(minheap, (dist[node] + d, nn))

            nextNode = None
            while minheap:
                nextNode = heapq.heappop(minheap)
                if nextNode[1] in visit:
                    nextNode = None
                else:
                    break

            if not nextNode:
                return -1

            dist[nextNode[1]] = nextNode[0]

            visit.add(nextNode[1])
            node = nextNode[1]

        return max(dist.values())

