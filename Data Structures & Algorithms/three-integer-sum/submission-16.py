class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # remove duplicates
        #nums = list(set(nums))

        # solve
        for i in nums:
            nums2 = nums.copy()
            nums2.remove(i)
            for j in nums2:
                nums3 = nums2.copy()
                nums3.remove(j)
                for k in nums3:
                    if i + j + k == 0:
                        triplet = sorted([i, j, k])
                        if triplet not in result:
                            result.append(triplet)

        return result