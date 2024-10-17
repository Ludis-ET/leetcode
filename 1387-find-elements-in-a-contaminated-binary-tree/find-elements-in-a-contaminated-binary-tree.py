# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.check = set()
        root.val = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                t = q.popleft()
                if t.left:
                    t.left.val = (t.val * 2) + 1
                    q.append(t.left)
                if t.right:
                    t.right.val = (t.val * 2) + 2
                    q.append(t.right)
                self.check.add(t.val)

    def find(self, target: int) -> bool:
        return target in self.check


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)