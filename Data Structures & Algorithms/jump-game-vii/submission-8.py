class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # dfs with visit set (only solve each position once)
        # based problem conditions


        furthest = 0
        q = deque()
        q.append(0)
        while q:
            i = q.popleft()

            if i == len(s) - 1:
                return True

            start = max(i + minJump, furthest)
            end = min(i + maxJump, len(s) - 1)

            for j in range(start, end + 1):
                if s[j] == '0':
                    q.append(j)

            furthest = max(furthest, end)

        return False