class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # O(n)
        # O(n)
        # count number each string
        # iterate until reach kth string w/ count = 1

        counts = Counter(arr)

        kth = 0
        for s in arr:
            if counts[s] == 1:
                kth += 1

            if kth == k:
                return s


        return ""