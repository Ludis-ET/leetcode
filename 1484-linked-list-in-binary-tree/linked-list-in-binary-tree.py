# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check(node, lst):
            if not node or not lst:
                return not lst
            if node.val != lst.val:
                return False
            return check(node.left, lst.next) or check(node.right, lst.next)
        def dfs(node):
            if not node:
                return False
            if node.val == head.val and check(node, head):
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
