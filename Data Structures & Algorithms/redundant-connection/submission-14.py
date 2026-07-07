class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # DSU
        # attempt to union nodes by edges as long as the DS (find) are not same
        
        N = len(edges)
        par = [i for i in range(N + 1)] # 1 labelled, reason for N + 1, 0 unused
        rank = [1] * (N + 1) 

        def find(n):
            if n == par[n]:
                return par[n]

            par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            # find roots
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            # smaller rank par = bigger rank, update bigger rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return[n1, n2]





            