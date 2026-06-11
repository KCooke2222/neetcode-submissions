class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)

        totalSum = 0
        res = 0
        for num in nums:
            prefix[totalSum] += 1
            totalSum += num

            if totalSum - k in prefix:
                res += prefix[totalSum - k]

        return res