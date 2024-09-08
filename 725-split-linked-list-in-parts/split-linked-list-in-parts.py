# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        counter = head
        while counter:
            count += 1
            counter = counter.next
        
        add = count % k
        div = count // k
        ans = []
        for _ in range(k):
            last = ListNode(0)
            way = last
            tmp = 0
            while head and tmp < div:
                way.next = ListNode(head.val)
                way = way.next
                head = head.next
                tmp += 1
            if add and head:
                way.next = ListNode(head.val)
                head = head.next
                add -= 1
            ans.append(last.next)
        return ans