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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return
            if not node.next: return TreeNode(node.val)
            f, s, p = node, node, None
            while f and f.next:
                p = s
                s = s.next
                f = f.next.next
            root = TreeNode(s.val)
            p.next = None
            root.right = dfs(s.next)
            root.left = dfs(node)
            return root
        return dfs(head)            