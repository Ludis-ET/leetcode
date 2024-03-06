# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans, nxt = ListNode(0), 0
        cur = ans
        while l1 or l2 or nxt > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            tmp = val1 + val2 + nxt
            if tmp < 10:
                cur.next = ListNode(tmp)
                cur, nxt = cur.next, 0
            else:
                t, m = divmod(tmp, 10)
                cur.next = ListNode(m)
                cur, nxt = cur.next, t
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ans.next