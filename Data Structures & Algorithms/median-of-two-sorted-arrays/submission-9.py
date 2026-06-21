class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(logn)
        # run on smaller by swapping nums1 and nums2 (ensures partitioning valid)
        # binary search is performed on one array 
            # other arrays left half = (total // 2) - (mid + 1)
            # we compare end of left half to other arr end left half + 1
        # run the binary search as needed until the crossing has <= for both crossings
            # take median depending on total being even or odd

        # also we are using default values to avoid edge cases (see code)

        A, B = nums1, nums2
        if B < A:
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = total // 2
        l, r = 0, m - 1


        while True:
            mid = (l + r) // 2
            mid2 = half - (mid + 1) - 1

            # crossing values
            Al = A[mid] if mid >= 0 else float("-inf")
            Ar = A[mid + 1] if mid + 1 < len(A) else float("inf")
            Bl = B[mid2] if mid2 >= 0 else float("-inf")
            Br = B[mid2 + 1] if mid2 + 1 < len(B) else float("inf")

            # adjusting crossing
            if not(Al <= Br):
                r = mid - 1

            elif not(Bl <= Ar):
                l = mid + 1

            else: # even and odd cases
                if total % 2 == 0:
                    return (max(Al, Bl) + min(Ar, Br)) / 2
                else:
                    return min(Ar, Br)

