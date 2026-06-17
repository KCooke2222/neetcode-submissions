class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # O(n)
        # scan to mark values with -1
        # 2 pointers: next gap, iteration
            # if next gap < iteration 
                # move iteration forward scan for next gap

        valueCount = 0 
        for i in range(len(nums)):
            if nums[i] == val:
                valueCount += 1
                nums[i] = -1

        gap = 0
        i = 0
        for i in range(len(nums)):
            while gap < len(nums) and nums[gap] != -1:
                gap += 1

            if gap < i:
                nums[gap] = nums[i]
                nums[i] = -1

        return len(nums) - valueCount
        