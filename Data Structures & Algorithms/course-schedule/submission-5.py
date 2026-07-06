class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # using global visist to track progress, local to find cycle on dfs

        adj = defaultdict(list)
        for p in prerequisites:
            adj[p[1]].append(p[0])

        visit = set()


        def dfs(p, lVisit):
            nonlocal visit

            if p in lVisit:
                return False

            visit.add(p)
            lVisit.add(p)

            res = True
            for c in adj.get(p, []):
                res = dfs(c, lVisit) and res

            lVisit.remove(p)

            return res

        for p in adj:
            if p not in visit:
                if not dfs(p, set()):
                    return False

        return True