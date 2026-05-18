# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def insert(node, val):
            nextNode = node.next
            node.next = ListNode(val, nextNode)

        def get_gcd(a, b):
            while b:
                a, b = b, a % b 
            return a

        cur = head
        while cur and cur.next != None:
            nextNode = cur.next

            # get gcd
            gcd = get_gcd(cur.val, nextNode.val)

            insert(cur, gcd)

            cur = cur.next.next

        return head