# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # getting the middle using fast and slow pointer
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reversing the next half 
        prev, cur = None , slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # checking the palindromity
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True