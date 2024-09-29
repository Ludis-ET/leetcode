class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(i, cur):
            if i == len(graph) - 1:
                ans.append(cur.copy())
                return
            for k in graph[i]:
                cur.append(k)
                dfs(k, cur)
                cur.pop()
        dfs(0, [0])
        return ans