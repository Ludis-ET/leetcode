# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def dfs(q):
            if not q: return
            root = TreeNode(int(q.popleft()[0]))
            if q:
                c = q.popleft()[1]
                l = deque()
                i = 0
                while i < len(q):
                    t = q.popleft()
                    if t[0] == '-' and t[1] == c:
                        break
                    l.append(t)
                root.left = dfs(l)
                root.right = dfs(q)
            return root


        q = deque()
        for i in traversal:
            if q and i == '-' and q[-1][0] == '-':
                q[-1][1] += 1
            elif i == '-':
                q.append(['-',1])
            elif not q or q[-1][0] == '-':
                q.append([i])
            else:
                q[-1][0] += i
        return dfs(q)