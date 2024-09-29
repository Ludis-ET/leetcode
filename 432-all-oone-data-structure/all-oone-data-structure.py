class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_count = {}
        self.count_node = {}

    def _insert_node_after(self, prev_node, new_node):
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node[node.count]

    def inc(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            node = self.count_node[count]
            node.keys.remove(key)
            if node.next.count != count + 1:
                new_node = Node(count + 1)
                self._insert_node_after(node, new_node)
                self.count_node[count + 1] = new_node
            node.next.keys.add(key)
            if not node.keys:
                self._remove_node(node)
            self.key_count[key] = count + 1
        else:
            if self.head.next.count != 1:
                new_node = Node(1)
                self._insert_node_after(self.head, new_node)
                self.count_node[1] = new_node
            self.head.next.keys.add(key)
            self.key_count[key] = 1

    def dec(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            node = self.count_node[count]
            node.keys.remove(key)
            if count > 1:
                if node.prev.count != count - 1:
                    new_node = Node(count - 1)
                    self._insert_node_after(node.prev, new_node)
                    self.count_node[count - 1] = new_node
                node.prev.keys.add(key)
                self.key_count[key] = count - 1
            else:
                del self.key_count[key]
            if not node.keys:
                self._remove_node(node)

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""
