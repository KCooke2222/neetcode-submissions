class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        memo = {}
        def dfs(nums):
            if tuple(nums) in memo:
                return memo[tuple(nums)]
            
            res = 0
            for i in range(len(nums)):
                if i == 0:
                    a = 1
                else:
                    a = nums[i - 1]
                if i == len(nums) - 1:
                    c = 1
                else:
                    c = nums[i + 1]

                burst = a * nums[i] * c
                res = max(res, burst + dfs(nums[0:i] + nums[i + 1:]))

            memo[tuple(nums)] = res
            return res

        return dfs(nums)