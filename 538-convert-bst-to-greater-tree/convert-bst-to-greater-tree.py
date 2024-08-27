# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            vals.append(node)
            dfs(node.right)
        dfs(root)
        for i in range(len(vals) - 2, -1, -1): vals[i].val += vals[i + 1].val
        return root
