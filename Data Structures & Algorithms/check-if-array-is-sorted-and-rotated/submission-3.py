class Solution:
    def check(self, nums: List[int]) -> bool:
        # O(n)
        # O(1)
        # find index max
        # iterate for len times from max, ensure increasing or equal to prev, else False

        def index(i):
            return i % len(nums)

        maxI = nums.index(max(nums))
        while nums[index(maxI)] == nums[index(maxI + 1)]:
            maxI += 1

        prev = None
        for i in range(len(nums)):
            cur = nums[index(maxI + 1 + i)]
            if prev and prev > cur:
                return False

            prev = cur

        return True
