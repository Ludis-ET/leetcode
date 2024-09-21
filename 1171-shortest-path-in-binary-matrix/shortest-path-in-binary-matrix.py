class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q, visited = deque(), set()
        if grid[0][0] == 1: return -1
        q.append((0, 0))
        visited.add((0, 0))
        ans = 1
        while q: 
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == row - 1 and c == col - 1:
                    return ans
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
                for dr, dc in dirs:
                    i, j = dr + r, dc + c
                    if min(i, j) < 0 or i == row or j == col or grid[i][j] == 1 or (i, j) in visited:
                        continue
                    q.append((i, j))
                    visited.add((i, j))
            ans += 1
        return -1