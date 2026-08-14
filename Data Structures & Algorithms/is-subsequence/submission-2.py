class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # O(n)
        # O(1)
        # if s bigger False
        # iterate over t, move as well when s = t

        if len(s) == 0:
            return True

        if len(s) > len(t):
            return False

        i = 0
        for c in t:
            if s[i] == c:
                i += 1
                if i == len(s):
                    return True

        return False
    