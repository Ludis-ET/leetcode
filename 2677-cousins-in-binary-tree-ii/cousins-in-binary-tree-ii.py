# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        root.val = 0
        while q:
            tmp, total = [], 0
            for _ in range(len(q)):
                t, u = q.popleft(), []
                if t.left: 
                    total += t.left.val
                    u.append(t.left)
                    q.append(t.left)
                if t.right: 
                    total += t.right.val
                    u.append(t.right)
                    q.append(t.right)
                if u: tmp.append(u)
            for i in range(len(tmp)):
                s = sum(i.val for i in tmp[i])
                for j in range(len(tmp[i])):
                    tmp[i][j].val = total - s
        return root