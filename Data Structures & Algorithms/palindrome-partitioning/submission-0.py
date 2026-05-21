class Solution:
    def isPali(self, s, i, j):
        while s[i] == s[j]:
            if j - i <= 1:
                return True
            i += 1
            j -= 1

        return False


    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            else:
                for j in range(i, len(s)):
                    if self.isPali(s, i, j):
                        part.append(s[i:j+1])
                        dfs(j+1)
                        part.pop()

        dfs(0)
        return res
