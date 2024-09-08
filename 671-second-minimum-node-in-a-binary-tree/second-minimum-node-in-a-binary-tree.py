# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        tmp = set()
        def dfs(node):
            if not node: return 
            tmp.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        ans = sorted(tmp)
        return -1 if len(ans) < 2 else ans[1]