# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # recursivally build the tree and subtrees
        # root is first in preorder, determine subtree sizes from in-order
            # connect root to left and right then return

        
        def dfs(prePos, inPos):
            pl, pr = prePos
            il, ir = inPos

            if pl > pr or il > ir:
                return None

            if pl < len(preorder):
                root = TreeNode(preorder[pl])
            else:
                return None

            iRoot = 0
            for i in range(il, ir + 1):
                if inorder[i] == preorder[pl]:
                    iRoot = i
                    break

            sizeL = iRoot - il
            sizeR = ir - iRoot

            root.left = dfs((pl + 1, pl + sizeL), (il, iRoot - 1))
            root.right = dfs((pl + sizeL + 1, pr), (iRoot + 1, ir))

            return root

        return dfs((0, len(preorder) - 1), (0, len(inorder) - 1))