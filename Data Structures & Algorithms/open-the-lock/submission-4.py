class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # O(d^n)
        # bfs with visit set

        n = len(target)

        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        visit = set()
        q = deque()
        q.append(([0] * n, 0))
        while q:
            cur, turns = q.popleft()

            for i in range(n):
                original = cur[i]

                for d in [-1, 1]:
                    cur[i] = (cur[i] + d) % 10

                    new = new = "".join(map(str, cur))
                    if new in visit or new in deadends:
                        cur[i] = original
                        continue

                    if new == target:
                        return turns + 1

                    visit.add(new)
                    q.append((cur[:], turns + 1))

                    cur[i] = original
        return -1