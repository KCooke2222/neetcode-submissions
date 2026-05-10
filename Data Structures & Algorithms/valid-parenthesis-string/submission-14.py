class Solution:
    def checkValidString(self, s: str) -> bool:
        lp_min = 0
        lp_max = 0

        for c in s:
            if c == "(":
                lp_min += 1
                lp_max += 1
            elif  c == ")":
                lp_min -= 1
                lp_max -= 1 
            elif c == "*":
                lp_min -= 1
                lp_max += 1
            
            if lp_max < 0:
                return False

            lp_min = max(lp_min, 0)

        return lp_min <= 0 and lp_max >= 0