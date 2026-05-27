class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # find if str1 + str2 = str2 + str1 (gcd exists)
        # find gcd of lengths

        if str1 + str2 == str2 + str1:
            g = math.gcd(len(str1), len(str2))
            return str1[:g]
        else:
            return ''
        