"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q, n = deque(), 0
        if root: q.append(root)
        while q:
            n += 1
            for _ in range(len(q)):
                for node in q.popleft().children:
                    q.append(node)
        return n