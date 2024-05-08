# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(0)
        right = ListNode(0)
        l, r = left, right
        while head:
            if head.val >= x:
                right.next = ListNode(head.val)
                right = right.next
            else:
                left.next = ListNode(head.val)
                left = left.next
            head = head.next
        left.next = r.next
        return l.next