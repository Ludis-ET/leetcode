# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        left = ListNode(0)
        right = ListNode(0)
        l, r = left, right
        while head:
            if n % 2 == 0:
                r.next = head
                r = r.next
            else:
                l.next = head
                l = l.next
            head = head.next
            n += 1
        r.next = None
        l.next = right.next
        return left.next