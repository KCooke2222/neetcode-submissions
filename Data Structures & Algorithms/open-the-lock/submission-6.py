class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # start 0000
        # bfs on each digit +1 and -1, store level
            # ensure is not in visit or deadend
        # if target is found return cur level
        # if q ends return -1

        deadends = set(deadends)

        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        q = deque(["0000"])
        visit = set(["0000"])
        level = 0

        while q:
            level += 1
            paths = q.copy()
            q = deque()

            for path in paths:
                for i in range(len(path)):
                    dirs = [1, -1]
                    for d in dirs:
                        digit = (int(path[i]) + d) % 10
                        newPath = path[:i] + str(digit) + path[i + 1:]

                        if newPath == target:
                            return level
                        if not newPath in visit and not newPath in deadends:
                            q.append(newPath)
                            visit.add(newPath)

        return -1