# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q, ans = deque([(root,'m')]), []
        while q:
            for _ in range(len(q)):
                t, p = q.popleft()
                if not t.left and not t.right:
                    ans.append((t.val, p))
                if t.left: q.append([t.left, 'l'])
                if t.right: q.append([t.right, 'r'])
        return sum(i for i, p in ans if p == 'l')