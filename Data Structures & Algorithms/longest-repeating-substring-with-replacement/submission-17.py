class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # store counts in size 26 array
        # create l and r pointer to form substrng window
        # if sum(counts) - max(counts) <= k
            # r++
            # increase res if new max substring
        # else
            # l++


        counts = [0] * 26
        l, r = 0, 0
        res = 0

        while r < len(s):
            counts[ord(s[r]) - ord('A')] += 1

            if (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res
        
            

