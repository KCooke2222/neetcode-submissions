class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dir = None
        for i in range(1, len(nums)):
            curDir = nums[i] - nums[i - 1]
            if curDir == 0:
                    continue
            
            if dir == None:
                
                dir = curDir
            else:
                if (dir > 0) != ( curDir > 0):
                    return False

        return True