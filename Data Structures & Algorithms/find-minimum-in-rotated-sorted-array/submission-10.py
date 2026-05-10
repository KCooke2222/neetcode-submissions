class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        min_v = float('inf')
        while l <= r:
            mid = (l + r) // 2

            min_v = min(min_v, nums[mid])
            if nums[l] <= nums[mid] <= nums[r]:
                return nums[l] 
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid 
        
        return min_v