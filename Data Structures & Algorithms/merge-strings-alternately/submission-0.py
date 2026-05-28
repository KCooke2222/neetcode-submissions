class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # iterate and merge

        res = []
        for i in range(max(len(word1), len(word2))):
            if i > len(word1) - 1:
                res.append(word2[i])
                continue

            if i > len(word2) - 1:
                res.append(word1[i])
                continue

            res.append(word1[i])
            res.append(word2[i])

        return "".join(res)