class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        target = totalSum // 2

        if totalSum % 2 != 0:
            return False

        memo = set([0])
        for num in nums:
            for n in memo.copy():
                new = n + num
                if new == target:
                    return True
                elif new < target:
                    memo.add(new)

        return False
            