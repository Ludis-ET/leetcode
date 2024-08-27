# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, prev, pos):
            self.ans = max(self.ans, prev)
            if not node:
                return
            if pos:
                dfs(node.left, prev + 1, 0)
                dfs(node.right, 0, 1)
            else:
                dfs(node.right, prev + 1, 1)
                dfs(node.left, 0, 0)
        dfs(root.right, 0, 1)
        dfs(root.left, 0, 0)
        return self.ans
