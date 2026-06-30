"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # O(n)
        # build linked list via next ptrs
            # also build original to copy hashmap
        # iterate again and assign copies random to nodeHash[original]

        if not head:
            return None

        nodeHash = {}

        headL2 = Node(head.val)
        l2 = headL2

        nodeHash[head] = l2

        l1 = head.next
        while l1:
            new = Node(l1.val)
            l2.next = new

            l2 = l2.next
            nodeHash[l1] = l2

            l1 = l1.next

        

        l2 = headL2
        l1 = head
        while l2:
            l2.random = nodeHash.get(l1.random)

            l2 = l2.next
            l1 = l1.next


        return headL2
