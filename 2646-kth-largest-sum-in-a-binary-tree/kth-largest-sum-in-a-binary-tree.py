# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        ans, q = [], deque([root])
        while q:
            total = 0
            for _ in range(len(q)):
                t = q.popleft()
                total += t.val
                if t.left: q.append(t.left)
                if t.right: q.append(t.right)
            ans.append(total)
        return -1 if k > len(ans) else sorted(ans, reverse=True)[k - 1]