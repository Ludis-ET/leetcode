class Trie:
    def __init__(self):
        self.children = {}
        self.last = False
        self.index = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = Trie()
        self.hp = []
        for i, word in enumerate(words):
            self._add(word, i)

    def f(self, pref: str, suff: str) -> int:
        self.hp.clear()
        prefix = self._pre(pref)
        if not prefix[0]: return -1
        self._dfs(pref, prefix[1])
        while self.hp:
            i, s = heapq.heappop(self.hp)
            if s[:len(suff)] == suff[::-1]:
                return -i
        return -1
    
    def _add(self, word, i) -> None:
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                tmp.children[c] = Trie()
            tmp = tmp.children[c]
        tmp.last = True
        tmp.index = i
    
    def _pre(self, pref):
        tmp = self.root
        for c in pref:
            if c not in tmp.children:
                return [False]
            tmp = tmp.children[c]
        return [True, tmp]

    def _dfs(self, prev, root):
        if root.last:
            heapq.heappush(self.hp,[-root.index, prev[::-1]])
        for c in root.children:
            self._dfs(prev + c, root.children[c])