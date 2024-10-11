class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = [0] * n
        for i, j in roads:
            graph[i] += 1
            graph[j] += 1
        
        label, ans = 1, 0
        for count in sorted(graph):
            ans += label * count
            label += 1
        
        return ans
        