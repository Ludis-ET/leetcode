# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q, ans = deque([root]), []
        while q:
            tot, n = 0, 0
            for _ in range(len(q)):
                t = q.popleft()
                tot += t.val
                n += 1
                if t.left: q.append(t.left)
                if t.right: q.append(t.right)
            ans.append(tot/n)
        return ans
