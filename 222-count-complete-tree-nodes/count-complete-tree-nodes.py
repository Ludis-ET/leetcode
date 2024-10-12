# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans, q = 0, deque()
        if root: q.append(root)
        while q:
            ans += len(q)
            for _ in range(len(q)):
                t = q.popleft()
                if t.right:q.append(t.right)
                if t.left: q.append(t.left)
        return ans