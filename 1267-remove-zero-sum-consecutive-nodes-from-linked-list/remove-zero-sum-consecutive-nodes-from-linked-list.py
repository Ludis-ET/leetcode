# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        table, prev = defaultdict(ListNode), 0
        dummy = ListNode(0)
        dummy.next = head
        table = {}
        curr = dummy
        prefix_sum = 0
        
        while curr:
            prefix_sum += curr.val
            table[prefix_sum] = curr
            curr = curr.next
        curr = dummy
        prefix_sum = 0
        while curr:
            prefix_sum += curr.val
            curr.next = table[prefix_sum].next
            curr = curr.next
        
        return dummy.next