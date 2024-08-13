# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            tmp = []
            for _ in range(len(q)):
                t = q.popleft()
                tmp.append(t.left.val if t != 1000 and t.left else 1000)
                tmp.append(t.right.val if t != 1000 and t.right else 1000)
                q.append(t.left if t != 1000 and t.left else 1000)
                q.append(t.right if t != 1000 and t.right else 1000)
            if len(set(tmp)) == 1 and tmp[0] == 1000: break
            mid = (len(tmp) - 1) // 2
            r = mid + 1
            while mid >= 0 and r < len(tmp):
                if tmp[mid] != tmp[r]: return False
                mid -= 1
                r += 1
        return True