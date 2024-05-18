# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0
        while l1:
            n1 = (n1 * 10) + l1.val
            l1 = l1.next
        
        while l2:
            n2 = (n2 * 10) + l2.val
            l2 = l2.next
        final = str(n1 + n2)

        res = ListNode(0)
        tmp = res
        for i in final:
            tmp.next = ListNode(int(i))
            tmp = tmp.next

        return res.next