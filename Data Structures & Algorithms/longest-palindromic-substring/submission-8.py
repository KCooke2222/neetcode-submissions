class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        # one center
        for c in range(len(s)):
            i = c
            j = c

            # expand palindrom outwards
            while i >= 0 and j <= len(s) - 1:
                if s[i] != s[j]:
                    break
                
                if j+1-i > len(res):
                    res = s[i:j+1]

                i -= 1
                j += 1


        # two center
        for c in range(len(s)):
            i = c
            j = c + 1

            # expand palindrom outwards
            while i >= 0 and j <= len(s) - 1:
                if s[i] != s[j]:
                    break
                
                if j+1-i > len(res):
                    res = s[i:j+1]

                i -= 1
                j += 1

        return res

            