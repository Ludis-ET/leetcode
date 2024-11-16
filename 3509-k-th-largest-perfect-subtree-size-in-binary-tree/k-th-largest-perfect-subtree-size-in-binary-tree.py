# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        hp = []
        def dfs(node):
            if not node:
                return [0, 0]
            l = dfs(node.left)
            r = dfs(node.right)
            if l[0] == r[0] and l[0] >= 0 and r[0] >= 0:
                heapq.heappush(hp, -(l[1] + r[1] + 1))
                return [l[0] + 1, l[1] + r[1] + 1]
            return [-1]
        dfs(root)
        while hp and k > 1:
            heapq.heappop(hp)
            k -= 1
        return -hp[0] if hp else -1
