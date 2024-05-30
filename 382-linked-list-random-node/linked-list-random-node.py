# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        tmp = self.head.val

        i = 2
        nxt = self.head.next
        while nxt:
            if random.random() < 1/i:
                tmp = nxt.val
            i += 1
            nxt = nxt.next
        return tmp

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()