class Trie:
    def __init__(self):
        self.children = {}
        self.last = False
        self.word = ""

class Solution:
    def add(self, trie, word) -> None:
        for i in word:
            if i not in trie.children:
                trie.children[i] = Trie()
            trie = trie.children[i]
        trie.last = True
        trie.word = word

    def backtrack(self, r, c, board, node, result) -> bool:
        char = board[r][c]
        if char not in node.children:
            return
        node = node.children[char]
        if node.last:
            result.append(node.word)
            node.last = False
        board[r][c] = '#'
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                if board[nr][nc] != '#':
                    self.backtrack(nr, nc, board, node, result)
        board[r][c] = char 


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for val in words:
            self.add(root, val)
        ans = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.children:
                    self.backtrack(r, c, board, root, ans)
        return ans
        
