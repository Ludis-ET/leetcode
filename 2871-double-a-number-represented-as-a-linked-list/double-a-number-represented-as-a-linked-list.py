# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = 0
        while head:
            rev *= 10
            rev += head.val
            head = head.next
        rev *= 2
        if rev == 0: return ListNode(0)
        ans = ListNode(0)
        test = ans
        while rev > 0:
            test.next = ListNode(rev % 10)
            rev //= 10
            test = test.next
        
        prev, cur = None , ans.next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev