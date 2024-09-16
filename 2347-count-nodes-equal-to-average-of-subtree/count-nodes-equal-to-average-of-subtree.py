# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: return [0, 0, 0]
            l, r = dfs(node.left), dfs(node.right)
            total, n = (node.val + l[0] + r[0]), (1 + l[1] + r[1])
            av, ans = total // n, l[2] + r[2]
            ans += (node.val == av)
            return [total, n, ans]
        return dfs(root)[2]