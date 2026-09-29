class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # basic 2d dp
        # memo: (i in nums, j in k)
        # each step choose each possible size for the current group
            # and dfs off that
        # return max if all nums processed, inf if exceed k first


        memo = {}
        def dfs(i, j):
            if i == len(nums) and j == k:
                return 0

            if i == len(nums):
                return float("inf")

            if j == k:
                return float("inf")

            if (i, j) in memo:
                return memo[(i, j)]

            res = float("inf")
            cur = 0
            for end in range(i, len(nums)):
                cur += nums[end]

                res = min(res, max(cur, dfs(end + 1, j + 1)))
            
            memo[(i, j)] = res

            return memo[(i, j)]

        return dfs(0, 0)
