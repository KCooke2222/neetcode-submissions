# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # dfs for p and q
        # pass if p and q is found back up the chain
        # first node that has both p and q return


        res = None

        def dfs(node):
            nonlocal res

            if node == None:
                return (False, False)

            foundP = node.val == p.val
            foundQ = node.val == q.val

            pl, ql = dfs(node.left)
            pr, qr = dfs(node.right)

            foundP = foundP or pl or pr
            foundQ = foundQ or ql or qr

            if foundP and foundQ and res is None:
                res = node

            return (foundP, foundQ)

        dfs(root)
        return res