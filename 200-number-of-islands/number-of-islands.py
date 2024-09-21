class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans, islands = 0, set()
        def dfs(r, c, islands):
            row, col = len(grid), len(grid[0])
            if min(r, c) < 0 or r == row or c == col or grid[r][c] == "0" or (r, c) in islands:
                return
            islands.add((r, c))
            dfs(r + 1, c, islands)
            dfs(r - 1, c, islands)
            dfs(r, c + 1, islands)
            dfs(r, c - 1, islands)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in islands and grid[i][j] != "0":
                    ans += 1
                    dfs(i, j, islands)
        return ans
            