class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # using quicksort
        # median of 3
        # move pivot to middle
        # recursive on new parts

        def quickSort(l, r):
            if r - l < 1:
                return

            if r - l == 1:
                if nums[l] > nums[r]:
                    swap(l, r)
                return

 


            pivot = medianOfThree(l, r)
            pivot = partition(l, r - 1, pivot)
            quickSort(l, pivot - 1)
            quickSort(pivot + 1, r)
            

        def medianOfThree(l, r):
            mid = (l + r) // 2

            # order 3 positions
            if nums[l] > nums[mid]:
                swap(l, mid)
            if nums[mid] > nums[r]:
                swap(r, mid)
            if nums[l] > nums[mid]:
                swap(l, mid)

            # setup pivot at end
            swap(r, r - 1)
            swap(r, mid)
            return r

        def partition(l, r, pivot):
            while True:
                while nums[l] < nums[pivot]:
                    l += 1
                while nums[r] > nums[pivot]:
                    r -= 1

                if l >= r:
                    break

                swap(l, r)
                l += 1
                r -= 1

            swap(pivot, l)
            return l
             

        def swap(a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp


        

        quickSort(0, len(nums) - 1)
        return nums