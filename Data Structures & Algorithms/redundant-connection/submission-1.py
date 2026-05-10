class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N+1)] # parent is self
        rank = [1] * (N + 1) # rank in the group (level in tree)

        # set parent to root parent
        # path compression
        def find(n):
            if n == par[n]:
                return par[n]

            par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False


            # adding the edge to the tree based on which
            # is higher rank in the group
            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else:
                par[p1] = par[p2]
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            # if forms cycle return
            if not union(n1, n2):
                return [n1, n2]




            