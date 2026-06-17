class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 
        # dfs backtracking
        # base i = len(s) - 1
            # sentence complete, return [""], building sentence back up
        # iterate through string building word
            # if matches a dict word, branch and repeat
            # append cur word to list of sentences


        memo = {}    
        def dfs(i):
            if i == len(s):
                return [""]

            if i in memo:
                return memo[i]

            
            cur = ""
            res = []
            while i < len(s):
                cur += s[i]

                if cur in wordDict:
                    sentences = dfs(i + 1)
                    for j in range(len(sentences)): # add word to sentences
                        if sentences[j] == "":
                            sentences[j] = cur
                        else:
                            sentences[j] = cur + " " + sentences[j]
                    res += sentences
                
                
                i += 1


            memo[i] = res
            return res

        return dfs(0)

        