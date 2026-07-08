class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # O()
        # sort whole ticket list
        # build adj list from sorted tickets
        # run dfs to find paths, until res = len(tickets) + 1
            # at each step use list.pop(i) to remove each dest 
                # add to res and dfs
            # if dfs is success we found first in lex order => return
            # then list.insert(i, v) to add back if path fails
                # remove from res
        # return res
        

        adj = defaultdict(list)
        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)

        res = ["JFK"]
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True

            temp = adj[node].copy()
            for i, v in enumerate(temp):
                adj[node].pop(i)
                res.append(v)
                if dfs(v): return True
                res.pop()
                adj[node].insert(i, v)

            return False

        dfs("JFK")
        return res