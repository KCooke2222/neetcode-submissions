# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # preorder with null markers
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if node == None:
                return "N"
            
            return ",".join([str(node.val), preorder(node.left), preorder(node.right)])

        return preorder(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        q = deque(data)

        def build():
            val = q.popleft()

            if val == "N":
                return None
            
            node = TreeNode(val)
            node.left = build()
            node.right = build()
            return node

        return build()

            
