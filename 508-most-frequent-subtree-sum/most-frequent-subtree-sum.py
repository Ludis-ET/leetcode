# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        ans, table, mx = [], defaultdict(int), float('-inf')
        def dfs(node):
            if not node: return 0
            t = node.val
            t += dfs(node.left)
            t += dfs(node.right)
            table[t] += 1
            return t
        dfs(root)
        for i, j in table.items():
            if j > mx: ans, mx = [i], j
            elif j == mx: ans.append(i)
        return ans