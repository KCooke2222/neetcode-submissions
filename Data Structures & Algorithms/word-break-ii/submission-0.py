class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 
        # dfs
        # base i = len(s) - 1
            # sentence complete, build list to sentence string, add to res
        # store current sentence as string list
        # iterate through string building word
            # if matches a dict word, branch and repeat

        res = []
        def dfs(i, cur):
            if i == len(s):
                res.append(" ".join(cur[:-1]))
            
            
            while i < len(s):
                cur[-1] += s[i]

                if cur[-1] in wordDict:
                    dfs(i + 1, cur + [""])
                
                i += 1

        dfs(0, [""])
        return res

        