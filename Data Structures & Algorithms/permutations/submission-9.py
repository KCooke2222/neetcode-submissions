class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(cur, selected):
            if len(cur) == len(nums):
                res.append(cur[:])  # copy
                return

            for i in range(len(nums)):
                if not selected[i]:
                    selected[i] = True
                    cur.append(nums[i])
                    rec(cur, selected)
                    cur.pop()
                    selected[i] = False

        rec([], [False] * len(nums))
        return res