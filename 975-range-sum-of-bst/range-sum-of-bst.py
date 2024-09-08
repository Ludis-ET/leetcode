# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans, q = 0, deque([root])
        while q:
            for _ in range(len(q)):
                t = q.popleft()
                if t.val >= low and t.val <= high: ans += t.val
                if t.left: q.append(t.left)
                if t.right: q.append(t.right)
        return ans