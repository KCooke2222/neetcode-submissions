class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        meet = slow

        slow1 = meet
        slow2 = nums[0]

        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]

        return slow1