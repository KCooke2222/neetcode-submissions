class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # O(n)
        # O(m)
        # get counts for c in chars
        # count chars for each string and compare, must be <= each step

        charsCounts = [0] * 26

        for c in chars:
            charsCounts[ord(c) - ord('a')] += 1

        res = 0
        for w in words:
            counts = [0] * 26
            valid = True
            for c in w:
                counts[ord(c) - ord('a')] += 1
                if counts[ord(c) - ord('a')] > charsCounts[ord(c) - ord('a')]:
                    valid = False
                    break

            if valid:
                res += len(w)


        return res
