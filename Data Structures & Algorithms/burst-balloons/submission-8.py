class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp, memo subsets as (l, r)
        # add extra 1s around nums
        # dfs
            # bounds: l > r
            # memo
            # try popping all balloons as last 
                # pop = nums[l - 1] * nums[i] * nums[r + 1]
                # remaining work = dfs(l, i-1) + dfs(i+1, r)
            # return maximum path


        memo = {}

        nums = [1] + nums + [1]

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            res = 0
            for i in range(l, r + 1):
                pop = nums[l - 1] * nums[i] * nums[r + 1]
                res = max(res, dfs(l, i-1) + pop + dfs(i+1, r))

            memo[(l, r)] = res
            return res

        return dfs(1, len(nums) - 2)