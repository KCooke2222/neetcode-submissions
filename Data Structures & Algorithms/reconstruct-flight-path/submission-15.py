class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # use sorted adj list to ensure lexographic order and quick search
        # dfs on next nodes till find working paths
        # compare lexographic order return smallest if multiple paths

        adj = defaultdict(list)
        count = defaultdict(Counter) # track count of same tickets (edges)

        for a, b in tickets:
            adj[a].append(b)
            count[a][b] += 1

        for a in adj:
            adj[a].sort()
            
        def dfs(cur, path):
            if len(path) == len(tickets) + 1: # last airport
                return path
            
            # first working path is auto lexographically smallest (sorted)
            for dest in adj[cur]:
                if count[cur][dest] > 0:
                    count[cur][dest] -= 1
                    res = dfs(dest, path + [dest])
                    
                    if res:
                        return res
                    count[cur][dest] += 1

            return None

        return dfs("JFK", ["JFK"])