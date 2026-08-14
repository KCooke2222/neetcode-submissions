class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # dictionary word to letter
        # letters set built during iteration
        # split s into words
        # iterate over words
            # determine results here if word already found and matches letter else...

        
        wordMap = {}
        letters = set()

        words = s.split()
        if len(pattern) != len(words):
            return False


        for i, w in enumerate(words):
            l = pattern[i]
            if w in wordMap:
                if l != wordMap[w]:
                    return False
            else:
                if l in letters:
                    return False
                else:
                    wordMap[w] = l
                    letters.add(l)

        return True
                