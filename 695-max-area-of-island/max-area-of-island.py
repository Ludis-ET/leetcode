class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0
        def dfs(r, c):
            row, col = len(grid), len(grid[0])
            if min(r, c) < 0 or r == row or c == col or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            ans = 1
            ans += dfs(r + 1, c)
            ans += dfs(r - 1, c)
            ans += dfs(r, c + 1)
            ans += dfs(r, c - 1)
            self.ans = max(self.ans, ans)
            return ans
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    dfs(r, c)
        return self.ans