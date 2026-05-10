class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # sort array
        nums.sort()

        # iterate
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # adjust j and k while j < k
            # add pair when j + k = -i
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    result.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                
                elif nums[j] + nums[k] > - nums[i]:
                    k -= 1

        return result