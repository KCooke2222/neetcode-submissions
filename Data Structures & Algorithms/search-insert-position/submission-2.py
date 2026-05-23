class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search with final comparison for possible index

        def binary(l, r):
            if l > r:
                return l 

            mid = (l + r) // 2

            if target < nums[mid]:
                return binary(l, mid - 1)
            elif target > nums[mid]:
                return binary(mid + 1, r)
            else:
                return mid

        return binary(0, len(nums) - 1)