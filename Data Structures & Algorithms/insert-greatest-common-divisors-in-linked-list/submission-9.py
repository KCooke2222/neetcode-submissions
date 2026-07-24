# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def insert(pos, val):
            temp = pos.next
            pos.next = ListNode(val, temp)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        cur = head
        while cur and cur.next:
            insert(cur, gcd(cur.val, cur.next.val))
            cur = cur.next.next

        return head
