class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # O(V + E)
        # O(V + E)
        # topological sort alg
        # create adj list prereq to courses
        # initialize indegree for each node
        # init q with 0 indegree nodes
        # while q, adjust indegrees of nodes
            # increment counter
            # add to q if == 0
        # if counter != # nodes, there must have been a cycle

        
        prereqs = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            prereqs[b].append(a)

        indegrees = {i: 0 for i in range(numCourses)}
        for courses in prereqs.values():
            for c in courses:
                indegrees[c] += 1

        q = deque()
        for c, indegree in indegrees.items():
            if indegree == 0:
                q.append(c)

        counter = 0
        while q:
            c = q.popleft()
            counter += 1

            for n in prereqs[c]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    q.append(n)

        if counter != len(prereqs):
            return False

        return True