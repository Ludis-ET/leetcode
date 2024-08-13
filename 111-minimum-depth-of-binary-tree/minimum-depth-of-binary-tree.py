# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        tot = float('inf')
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l: tot = min(tot, l)
        if r: tot = min(tot, r)
        return 1 + (tot if tot != float('inf') else 0)