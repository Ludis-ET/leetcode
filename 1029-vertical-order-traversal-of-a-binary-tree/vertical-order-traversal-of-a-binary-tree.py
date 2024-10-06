# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        table = defaultdict(list)
        def dfs(node, r, c):
            if not node:
                return
            table[c].append([r, node.val])
            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)
        dfs(root, 0, 0)
        res = []
        for k in sorted(table.keys()):
            print(table[k])
            res.append([j for i, j in sorted(table[k])])
        return res