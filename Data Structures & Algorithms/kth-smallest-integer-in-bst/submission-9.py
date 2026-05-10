# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        i = 1
        def inorder(node):
            nonlocal k
            nonlocal i

            if not node:
                return

            ans = inorder(node.left)
            if ans is not None:
                return ans

            if i == k:
                return node.val
            i += 1


            return inorder(node.right)
        

        return inorder(root)
        
        