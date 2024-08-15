# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, prev):
            if not node:
                return
            if not node.left and not node.right:
                ans.append(prev + str(node.val))
                return
            cur = prev + str(node.val) + "->"
            dfs(node.left, cur)
            dfs(node.right, cur)
        dfs(root, "")
        return ans