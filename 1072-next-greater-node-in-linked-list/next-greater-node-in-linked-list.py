# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans, stack = [], []
        c = 0
        while head:
            ans.append(0)
            while stack and stack[-1][0] < head.val:
                a, b = stack.pop()
                ans[b] = head.val
            stack.append([head.val, c])
            head = head.next
            c += 1
        return ans
