# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        while head and head.next:
            node = ListNode(math.gcd(head.val, head.next.val))
            tmp = head.next
            head.next = node
            node.next = head = tmp
        return ans