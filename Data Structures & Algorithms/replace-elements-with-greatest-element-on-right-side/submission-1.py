class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # O(n)
        # O(1)
        # iterate backwards
        # store max so far and replace

        maxNum = None
        for i in range(len(arr) - 1, -1, -1):
            cur = arr[i]
            if maxNum is None:
                arr[i] = -1
                maxNum = cur
            else:
                arr[i] = maxNum
                maxNum = max(maxNum, cur)

        return arr
            