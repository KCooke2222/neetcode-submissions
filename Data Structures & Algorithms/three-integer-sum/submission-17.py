class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        if triplet not in seen:
                            seen.add(triplet)
                            result.append(list(triplet))

        return result
