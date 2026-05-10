class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(cur, nums):
            if not nums and cur:
                res.append(cur)
                return

            for i in range(len(nums)):
                rec(cur + [nums[i]], nums[:i] + nums[i+1:])

        rec([], nums)

        return res