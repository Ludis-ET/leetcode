# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = second = head
        while first and first.next != None:
            second = second.next
            first = first.next.next
            if second == first:
                return True
        return False
        