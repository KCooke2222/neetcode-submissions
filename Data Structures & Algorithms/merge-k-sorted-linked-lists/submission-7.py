# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        res = None
        cur = None


        for i, list in enumerate(lists):
            if list:
                heapq.heappush(q, (list.val, i))
                lists[i] = lists[i].next

        while q:
            val, i = heapq.heappop(q)
            
            if not res:
                res = ListNode(val)
                cur = res
            else:
                cur.next = ListNode(val)
                cur = cur.next

            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next

        return res
        