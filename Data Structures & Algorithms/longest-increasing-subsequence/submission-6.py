class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp with memo LIS
        # dfs from each num in loop
            # iterate until cur < next
            # return LIS = 1 + dfs(next)

        memo = {}

        def dfs(cur):
            if cur in memo:
                return memo[cur]

            nextPath = 0
            for i in range(cur + 1, len(nums)):
                if nums[cur] < nums[i]:
                    nextPath = max(nextPath, dfs(i))

            memo[cur] = 1 + nextPath

            return memo[cur]
        
        return max(dfs(i) for i in range(len(nums)))
                    