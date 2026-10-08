class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse array
        # reverse the front and back sub arrays
        # size k front, n - k back

        n = len(nums)
        k = k % n

        def reverse(arr, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)