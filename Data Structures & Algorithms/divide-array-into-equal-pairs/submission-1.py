class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # O(n)
        # O(n)
        # counter, counts must be even

        counts = Counter(nums)
        for c in counts.values():
            if c % 2 == 1:
                return False

        return True