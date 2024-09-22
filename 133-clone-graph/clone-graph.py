"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        check = {}
        def dfs(node):
            if node in check:
                return check[node]
            
            copy = Node(node.val)
            check[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node) if node else None