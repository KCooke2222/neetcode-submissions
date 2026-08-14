class Solution:
    def check(self, nums: List[int]) -> bool:
        # O(n)
        # O(1)
        # if more than one breakpoint where prev > cur, not sorted proper
        # iterate finding if count prev > cur is more than 1

        count = 0
        
        prev = nums[-1]
        for cur in nums:
            if prev > cur:
                count += 1
            prev = cur

        return count <= 1

        
