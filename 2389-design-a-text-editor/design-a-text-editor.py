class Node:
    def __init__(self, val=''):
        self.val = val
        self.prev = None
        self.next = None

class TextEditor:

    def __init__(self):
        self.head = Node('head')
        self.tail = Node('tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.head

    def addText(self, text: str) -> None:
        for char in text:
            node = Node(char)
            node.prev = self.cursor
            node.next = self.cursor.next
            self.cursor.next.prev = node
            self.cursor.next = node
            self.cursor = node

    def deleteText(self, k: int) -> int:
        delete_count = 0
        while k > 0 and self.cursor != self.head:
            prev_node = self.cursor.prev
            prev_node.next = self.cursor.next
            self.cursor.next.prev = prev_node
            self.cursor = prev_node
            k -= 1
            delete_count += 1
        return delete_count

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.cursor != self.head:
            self.cursor = self.cursor.prev
            k -= 1
        return self._get_last()

    def cursorRight(self, k: int) -> str:
        while k > 0 and self.cursor.next != self.tail:
            self.cursor = self.cursor.next
            k -= 1
        return self._get_last()

    def _get_last(self) -> str:
        result = []
        temp_cursor = self.cursor
        for _ in range(10):
            if temp_cursor == self.head:
                break
            result.append(temp_cursor.val)
            temp_cursor = temp_cursor.prev
        return ''.join(reversed(result))
