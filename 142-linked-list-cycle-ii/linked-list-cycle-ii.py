# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        if not fast or not fast.next: return None
        slow2 = head
        while slow != slow2: slow, slow2 = slow.next, slow2.next
        return slow