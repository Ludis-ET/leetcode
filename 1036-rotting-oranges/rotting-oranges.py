class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q, dirs = deque(), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ans, fresh = 0, 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    i, j = dr + r, dc + c
                    if min(i, j) < 0 or i == row or j == col or grid[i][j] != 1:
                        continue
                    grid[i][j] = 2
                    fresh -= 1
                    q.append([i, j])
            ans += 1
        return ans if not fresh else -1
