# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # divide and conquer
        # each node finds total_max and max including itself
            # total_max = max(left, right, max_including)
            # max_including = max (left, right max including) + node.val
        # res = roots total_max


        def dfs(node):
            if node == None:
                return (float("-inf"), 0) # max, max_incuding_node

            left_max, left_max_include = dfs(node.left)
            right_max, right_max_include = dfs(node.right)

            max_including = max(left_max_include, right_max_include, 0) + node.val
            max_through = max(left_max_include, 0) + max(right_max_include, 0) + node.val
            total_max = max(left_max, right_max, max_including, max_through)

            return (total_max, max_including)

        return dfs(root)[0]

