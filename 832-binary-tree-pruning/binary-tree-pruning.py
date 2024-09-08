# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return 0 
            l = dfs(node.left)
            r = dfs(node.right)
            if not l and not r: 
                node.left = node.right = None
                return node.val
            if not l: node.left = None
            if not r: node.right = None
            return 1
        return root if dfs(root) else None