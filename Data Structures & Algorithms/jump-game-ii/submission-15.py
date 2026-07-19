class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(nums) - 1:
            jump = 0
            for i in range(l, r + 1):
                jump = max(jump, i + nums[i])

            l = r
            r = jump
            res += 1

        return res