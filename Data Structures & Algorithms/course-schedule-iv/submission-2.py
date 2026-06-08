class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build adj list pre-req to course
        # run bfs to flatten each pre-reqs connection to set
        # query is now O(1)

        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)


        flattened = defaultdict(set)

        for a in adj:
            q = deque()
            q.append(a)
            while q:
                course = q.popleft()
                for child in adj.get(course, []):
                    if child not in flattened[a]:
                        q.append(child)
                        flattened[a].add(child)

        answer = []
        for pre, course in queries:
            if course in flattened[pre]:
                answer.append(True)
            else:
                answer.append(False)


        return answer






        