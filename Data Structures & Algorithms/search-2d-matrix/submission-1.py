class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [num for row in matrix for num in row]
        min = 0
        max = len(nums) - 1

        while min <= max:
            i = (min + max) // 2
            if nums[i] == target:
                return True
            elif nums[i] > target:
                max = i - 1
            else:
                min = i + 1

        return False  # target not found