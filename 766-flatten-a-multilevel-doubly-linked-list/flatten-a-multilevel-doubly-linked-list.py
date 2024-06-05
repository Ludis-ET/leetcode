"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = ListNode(0)
        ans = dummy

        if not head:
            return head

        def end(head, end):
            tmp = head
            while head.next:
                head = head.next
            head.next = end
            if end:
                end.prev = head
            return tmp

        while head:
            ans.next = head
            tmp = ans
            ans = ans.next
            ans.prev = tmp
            if head.child:
                tmp = head.next
                head.next = end(head.child, tmp)
                head.child = None
            head = head.next
        dummy = dummy.next
        dummy.prev = None
        return dummy