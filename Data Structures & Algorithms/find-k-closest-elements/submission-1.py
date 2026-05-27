class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find pos of first element
        # expand l and r ptr based on comparison logic
        # return array[l:r+1]

        def closer(a, b):
            if abs(a - x) < abs(b - x) or abs(a - x) == abs(b - x):
                return True
            else:
                return False

        i = 0
        while i < len(arr) - 1 and x > arr[i]:
            i += 1

        if i > 0 and closer(arr[i - 1], arr[i]):
            i = i - 1
        else:
            i = i

        l, r = i, i

        for i in range(k - 1):
            if r >= len(arr) - 1:
                l -= 1
                continue

            if l <= 0:
                r += 1
                continue

            if closer(arr[l - 1], arr[r + 1]):
                l -= 1
            else:
                r += 1

        return arr[l:r+1]

            