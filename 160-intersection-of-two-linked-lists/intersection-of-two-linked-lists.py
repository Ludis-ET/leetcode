# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length1 = length2 = 0
        tmp1, tmp2 = headA, headB

        while tmp1:
            length1 += 1
            tmp1 = tmp1.next

        while tmp2:
            length2 += 1
            tmp2 = tmp2.next

        while length1 > length2:
            headA = headA.next
            length1 -= 1

        while length2 > length1:
            headB = headB.next
            length2 -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None