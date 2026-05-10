class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(cur, nums, selected):
            if len(cur) == len(nums):
                res.append(cur)
                return

            for i in range(len(nums)):
                if not selected[i]:
                    selected[i] = True
                    rec(cur + [nums[i]], nums, selected)
                    selected[i] = False

        rec([], nums, [False] * len(nums))

        return res