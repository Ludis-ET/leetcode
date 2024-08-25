class Trie:
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    def add(self, word, root):
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.word = word  
    
    def dfs(self, node, result):
        if node.word:
            result.append(node.word)
        for char in sorted(node.children.keys()): 
            if len(result) < 3: 
                self.dfs(node.children[char], result)

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for product in products:
            self.add(product, root)
        
        ans = []
        node = root
        for char in searchWord:
            if char in node.children:
                node = node.children[char]
                suggestions = []
                self.dfs(node, suggestions)
                ans.append(suggestions)
            else:
                break
        while len(ans) < len(searchWord):
            ans.append([])
        return ans
