class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        target = totalSum // 2

        if totalSum % 2 != 0:
            return False

        memo = set([0])
        for num in nums:
            for n in memo.copy():
                memo.add(n + num)
                if n + num == target:
                    return True

        return False
            