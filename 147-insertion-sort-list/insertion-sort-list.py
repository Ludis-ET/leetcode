# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        nxt = head.next
        dummy.next = ListNode(head.val)
        while nxt:
            start = dummy.next
            prev = None
            while nxt and start and nxt.val > start.val:
                prev = start
                start = start.next
            if not start:
                prev.next = ListNode(nxt.val)
            else:
                node = ListNode(start.val, start.next)
                start.next = node
                start.val = nxt.val
            nxt = nxt.next
        return dummy.next
