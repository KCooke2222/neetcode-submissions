class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use l and r pointer on ends 
        # remove l or r dependent on which is further
        # shrink until size k is reached

        l, r = 0, len(arr) - 1

        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1

        return arr[l:r+1]

    

        