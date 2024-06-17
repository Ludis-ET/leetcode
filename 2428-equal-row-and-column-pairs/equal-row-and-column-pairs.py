class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans, n = 0, len(grid)
        normal = defaultdict(int)
        for i in grid:
            normal[tuple(i)] += 1

        other = [[grid[i][j] for i in range(n)] for j in range(n)]
        
        for i in other:
            ans += normal[tuple(i)]
        return ans
