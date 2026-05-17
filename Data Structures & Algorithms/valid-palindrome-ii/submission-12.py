class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1

        def is_palindrome(s, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else: 
                    return False
            return True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if is_palindrome(s, l + 1, r):
                    return True
                    
                if is_palindrome(s, l, r - 1):
                    return True
                
                return False

        return True


