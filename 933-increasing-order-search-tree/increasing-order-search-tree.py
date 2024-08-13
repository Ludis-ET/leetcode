# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(TreeNode(node.val))
            dfs(node.right)
        dfs(root)
        for i in range(1, len(ans)):
            ans[i - 1].right = ans[i]
        return ans[0]

