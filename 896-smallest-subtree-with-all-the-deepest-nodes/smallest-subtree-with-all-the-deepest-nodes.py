# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return [0, None]
            l = dfs(node.left)
            r = dfs(node.right)
            l[0] += 1
            r[0] += 1
            if l[0] == r[0]:
                return [l[0], node]
            return l if l[0] > r[0] else r
        return dfs(root)[1]
