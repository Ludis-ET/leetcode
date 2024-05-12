"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        table = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            table[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = table[cur]
            copy.next = table[cur.next]
            copy.random = table[cur.random]
            cur = cur.next
        
        return table[head]