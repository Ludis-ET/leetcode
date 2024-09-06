# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        rem = set(nums)
        prev = ListNode(0)
        ans = prev
        while head:
            if head.val not in rem:
                prev.next = ListNode(head.val)
                prev = prev.next
            head = head.next
        return ans.next