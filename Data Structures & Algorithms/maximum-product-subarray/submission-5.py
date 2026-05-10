class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMax, curMin = 1, 1
        for num in nums:
            if num == 0:
                curMax = 1
                curMin = 1    
                continue

            prodMax = curMax * num
            prodMin = curMin * num

            curMin = min(prodMax, prodMin, num)
            curMax = max(prodMax, prodMin, num)

            res = max(res, curMax)

        return res