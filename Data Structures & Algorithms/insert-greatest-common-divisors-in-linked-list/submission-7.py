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

        cur = head
        while cur and cur.next != None:
            nextNode = cur.next

            # get gcd
            gcd = 1
            for i in range(1, min(cur.val, nextNode.val) + 1):
                if cur.val % i == 0 and nextNode.val % i == 0:
                    gcd = i

            insert(cur, gcd)

            cur = cur.next.next

        return head