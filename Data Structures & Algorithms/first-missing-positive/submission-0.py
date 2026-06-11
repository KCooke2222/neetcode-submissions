class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(n)
        # smallest pos int must be btw 1 and len(nums) + 1
        # clean negatie values (set to 0 (nuetral))
        # for each num mark its index position (num - 1) as negative in the array
            # for 0s set to -(len(nums) + 1)
        # reiterate find smallest index non-negative num

        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0

        for i, num in enumerate(nums):
            num = abs(num)
            if 0 < num <= len(nums):
                if nums[num - 1] == 0:
                    nums[num - 1] = -1 * (len(nums) + 1)
                else:
                    nums[num - 1] = -1 * abs(nums[num - 1])

        for i, num in enumerate(nums):
            if num >= 0:
                return i + 1

        return len(nums) + 1