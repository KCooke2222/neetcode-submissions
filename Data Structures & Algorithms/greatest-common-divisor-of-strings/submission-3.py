class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # find divisors of str2
        # try on str1

        def checkDivisor(str1, str2):
            if len(str1) % len(str2) != 0:
                return False

            for i in range(len(str1)):
                if str1[i] != str2[i % len(str2)]:
                    return False

            return True

        for i in range(len(str2)):
            if checkDivisor(str2, str2[0:len(str2) - i]): # greatest to smallest divisor of str2
                if checkDivisor(str1, str2[0:len(str2) - i]):
                    return str2[0:len(str2) - i]

        

        return ""
        