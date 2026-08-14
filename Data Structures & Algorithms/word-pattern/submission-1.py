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
            if w in wordMap:
                if pattern[i] != wordMap[w]:
                    return False
            else:
                if pattern[i] in letters:
                    return False
                else:
                    wordMap[w] = pattern[i]
                    letters.add(pattern[i])

        return True
                