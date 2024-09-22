class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        table = defaultdict(list)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if not table[node]:
                return True
            visited.add(node)
            for i in table[node]:
                if not dfs(i): return False
            table[node] = []
            visited.remove(node)
            return True
        for pre, c in prerequisites:
            table[c].append(pre)

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True