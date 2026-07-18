class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp with memo LIS
        # dfs from each num in loop
            # iterate until cur < next
            # return LIS = 1 + dfs(next)

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            LIS = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            memo[i] = LIS
            return LIS
        
        return max(dfs(i) for i in range(len(nums)))
                    