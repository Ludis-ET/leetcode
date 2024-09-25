class Trie:
    def __init__(self):
        self.val = 0
        self.children = {}

class Solution:
    def addToTree(self, words):
        root = Trie()
        for word in words:
            tmp = root
            for c in word:
                if c not in tmp.children:
                    tmp.children[c] = Trie()
                tmp.children[c].val += 1
                tmp = tmp.children[c]
        return root

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = self.addToTree(words)
        ans = []
        for word in words:
            tmp, res = root, 0
            for c in word:
                res += tmp.children[c].val
                tmp = tmp.children[c]
            ans.append(res)
        return ans