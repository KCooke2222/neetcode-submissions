class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # hashmap counts chars in "balloon"
        # count chars in text
        # take lowest // count char in balloon

        balloon = Counter("balloon")
        text = Counter(text)

        res = float("inf")
        for c in balloon:
            count = text[c] // balloon[c]
            res = min(res, count)

        return res
