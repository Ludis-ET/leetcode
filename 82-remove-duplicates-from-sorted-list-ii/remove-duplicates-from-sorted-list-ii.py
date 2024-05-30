# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(0)
        ans = tmp
        while head and head.next:
            if head.val != head.next.val:
                tmp.next = ListNode(head.val)
                tmp = tmp.next
                head = head.next
            else:
                x = head.val
                while head and x == head.val:
                    head = head.next

        if head and  head.val != tmp.val:
            tmp.next = ListNode(head.val)
        return ans.next
