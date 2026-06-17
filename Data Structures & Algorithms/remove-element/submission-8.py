class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # O(n)
        # swap target values with last values in the array

        r = len(nums) - 1
        l = 0
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1

        return r + 1
        