class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new = nums[-k % len(nums):] + nums[:(len(nums) - k) % len(nums)]
        for i in range(len(nums)):
            nums[i] = new[i]
        