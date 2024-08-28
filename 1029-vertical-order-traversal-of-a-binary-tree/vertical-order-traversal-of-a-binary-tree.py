# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, table = [], defaultdict(list)
        def dfs(node, x, y):
            if not node:
                return
            table[x].append([y, node.val])
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)
        dfs(root, 0, 0)
        for i in sorted(table.keys()):
            ans.append([i for _, i in sorted(table[i])])
        return ans