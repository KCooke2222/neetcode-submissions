class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # O(n)
        # O(1)
        # iterate backwards
        # store max so far and replace

        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans
            