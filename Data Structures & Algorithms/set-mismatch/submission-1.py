class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # counts, item with 2 is dup
        # set, iterate until missing item

        counts = {}
        dup = None
        for n in nums:
            if n in counts:
                dup = n
            else:
                counts[n] = 1

        nSet = {n for n in nums}
        missing = None
        for i in range(1, len(nums) + 1):
            if i not in nSet:
                missing = i

        return [dup, missing]