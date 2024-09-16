# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nodes = []
        def bfs(node):
            q = deque()
            if node: q.append(node)
            while q:
                for _ in range(len(q)):
                    t = q.popleft()
                    heapq.heappush(nodes, t.val)
                    if t.left: q.append(t.left)
                    if t.right: q.append(t.right)
        bfs(root1)
        bfs(root2)
        ans = []
        while nodes:
            ans.append(heapq.heappop(nodes))
        return ans