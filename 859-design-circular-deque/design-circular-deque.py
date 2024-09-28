class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.l = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.k == self.l:
            return False
        node = Node(value, self.head, self.head.next)
        self.head.next.prev = node
        self.head.next = node
        self.l += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.k == self.l:
            return False
        node = Node(value, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.l += 1
        return True
        
    def deleteFront(self) -> bool:
        if self.l == 0:
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.l -= 1
        return True
        
    def deleteLast(self) -> bool:
        if self.l == 0:
            return False
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.l -= 1
        return True

    def getFront(self) -> int:
        if self.l == 0:
            return -1
        return self.head.next.val
        

    def getRear(self) -> int:
        if self.l == 0:
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.l == 0

    def isFull(self) -> bool:
        return self.l == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()