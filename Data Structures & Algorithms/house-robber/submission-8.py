class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            cur = max(rob1, num + rob2)
            rob2 = rob1
            rob1 = cur

        return max(rob1, rob2)
