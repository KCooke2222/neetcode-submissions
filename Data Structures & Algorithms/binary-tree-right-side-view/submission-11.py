# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs with level orders
        # as last item of the level is operated on (check next for diff level)
            # add this to the right side list

        if not root:
            return []

        res = []

        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

            if not q or level != q[0][1]:
                res.append(node.val)


        return res