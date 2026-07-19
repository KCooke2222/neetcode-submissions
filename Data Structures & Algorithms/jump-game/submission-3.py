class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # maintain furthest valid pos
        # iterate through array while updating furthest
        # if cur > furthest: false

        furthest = 0
        for i in range(len(nums)):
            if i > furthest:
                return False

            furthest = max(furthest, i + nums[i])

        return True