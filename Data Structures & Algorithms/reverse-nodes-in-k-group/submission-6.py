# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find kth node in section and link prev first node to kth
            # if not k nodes in the section just link prev_first to first of k
        # reverse section of k nodes
        # store first node in the chain to link back to next section
            
        
        prev_first = None
        cur_first = head
        first_kth = None

        while(True):
            kth = None
            cur = cur_first
            for i in range(k - 1):
                if cur == None:
                    break
                cur = cur.next

            kth = cur

            if not first_kth:
                first_kth = kth

            cur = cur_first
            prev = None
            if kth:
                for i in range(k):
                    next_node = cur.next
                    cur.next = prev
                    prev = cur
                    cur = next_node # cur = prev_first
                if prev_first:
                    prev_first.next = kth
                prev_first = cur_first
                cur_first = cur
            else:
                prev_first.next = cur_first
                break

        return first_kth if first_kth else head