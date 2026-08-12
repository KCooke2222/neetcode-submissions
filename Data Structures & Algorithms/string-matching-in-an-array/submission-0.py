class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # O(n^2 * m^2) - m is characters in str
        # O(1)
        # sort strings
        # compare smaller str in bigger strings

        words.sort(key = lambda s: len(s))

        res = []
        for i in range(len(words)):
            substring = False
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    substring = True
                    break

            if substring:
                res.append(words[i])


        return res