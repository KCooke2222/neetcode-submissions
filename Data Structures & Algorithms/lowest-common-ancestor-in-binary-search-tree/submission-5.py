# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root

        while (p.val < res.val) == (q.val < res.val) and not (q.val == res.val or p.val == res.val):
            if p.val < res.val:
                res = res.left
            else:
                res = res.right
        
        return res