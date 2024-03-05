class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        while head and head.next:
            if head.val == head.next.val:
                new_head = head.next.next
                head.next = new_head
            else:
                head = head.next
        return root