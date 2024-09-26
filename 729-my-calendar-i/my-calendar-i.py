class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node([start, end])
            return True
        return self.dfs([start, end], self.root)[1]

    def dfs(self, event, node):
        if not node:
            return [Node(event), True]
        s, e = event
        if s >= node.val[1]:
            node.right, success = self.dfs(event, node.right)
        elif e <= node.val[0]:
            node.left, success = self.dfs(event, node.left)
        else:
            return [node, False]
        return [node, success]
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
