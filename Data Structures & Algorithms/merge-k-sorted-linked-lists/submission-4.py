# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # until all lists empty
        # add smallest element to our list 
        # return the list
        if not any(lists):
            return None

        head = None

        i = min([(head.val, i) for i, head in enumerate(lists) if head is not None])[1]
        new_node = lists[i]
        lists[i] = lists[i].next

        head = new_node
        cur = head

        while any(lists):
            i = min([(head.val, i) for i, head in enumerate(lists) if head is not None])[1]
            new_node = lists[i]
            lists[i] = lists[i].next

            cur.next = new_node
            cur = cur.next

        return head

