class Trie:
    def __init__(self):
        self.children = {}
        self.is_last = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans, root = [], Trie()
        def append(folder):
            node = root
            for path in folder.split('/'):
                if len(path):
                    if path not in node.children:
                        node.children[path] = Trie()
                    node = node.children[path]
            node.is_last = True

        def check(folder):
            folder.pop()
            node = root
            for i in range(1, len(folder)):
                path = folder[i]
                if path in node.children and node.children[path].is_last:
                    return False
                node = node.children[path]
            return True

        for path in folder:
            append(path)

        for path in folder:
            if check(path.split('/')):
                ans.append(path)
        return ans