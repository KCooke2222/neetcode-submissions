class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # res tracks combs
        # dfs through all combs
            # if len digits == len path add to res

        res = []
        path = []
        chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            if i >= len(digits):
                if len(path) > 0:
                    res.append("".join(path))
                return

            for c in chars[digits[i]]:
                path.append(c)
                dfs(i + 1)
                path.pop()
            
        dfs(0)
        return res
