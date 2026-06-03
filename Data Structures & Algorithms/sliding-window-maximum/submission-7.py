class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        l = 0
        for i, v in enumerate(nums):
            while dq and nums[dq[-1]] < v:
                dq.pop()
            dq.append(i)

            if l > dq[0]:
                dq.popleft()

            if i >= k - 1:
                res.append(nums[dq[0]])
                l += 1

            


        return res

