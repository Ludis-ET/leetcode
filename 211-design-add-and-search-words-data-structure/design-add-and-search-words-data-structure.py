class Trie:
    def __init__(self):
        self.children = {}
        self.last = False

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        tmp = self.trie
        for k in word:
            if k not in tmp.children:
                tmp.children[k] = Trie()
            tmp = tmp.children[k]
        tmp.last = True

    def backtrack(self, trie, word) -> bool:
        for c, k in enumerate(word):
            if k == '.':
                for i in trie.children:
                    if self.backtrack(trie.children[i], word[c + 1:]):
                        return True
            if k not in trie.children:
                return False
            trie = trie.children[k]
        return trie.last

    def search(self, word: str) -> bool:
        return self.backtrack(self.trie, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)