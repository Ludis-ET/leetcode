# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque([root])

    def insert(self, val: int) -> int:
        while self.q:
            for _ in range(len(self.q)):
                t = self.q.popleft()
                get = False
                if not t.left:
                    t.left = TreeNode(val)
                    get = 1
                elif not t.right:
                    t.right = TreeNode(val)
                    get = 1
                if t.left: self.q.append(t.left)
                if t.right: self.q.append(t.right)
                if get:
                    self.q.appendleft(t)
                    return t.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()