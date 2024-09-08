# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, pre):
            if not node: return 1
            if node.val != pre: return 0
            return dfs(node.left, node.val) and dfs(node.right, node.val)
        return dfs(root, root.val)
