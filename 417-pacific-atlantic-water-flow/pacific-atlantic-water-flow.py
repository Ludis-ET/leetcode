class Solution:
    def pacificAtlantic(self, he: List[List[int]]) -> List[List[int]]:
        rows, cols = len(he), len(he[0])
        pac, atl = set(), set()

        def dfs(r, c, ocean, prev):
            if min(r, c) < 0 or r == rows or c == cols or he[r][c] < prev or (r, c) in ocean:
                return
            ocean.add((r, c))
            dfs(r + 1, c, ocean, he[r][c])
            dfs(r - 1, c, ocean, he[r][c])
            dfs(r, c - 1, ocean, he[r][c])
            dfs(r, c + 1, ocean, he[r][c])

        for c in range(cols):
            dfs(0, c, pac, he[0][c])
            dfs(rows - 1, c, atl, he[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, he[r][0])
            dfs(r, cols - 1, atl, he[r][cols - 1])

        ans = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r, c])
        return ans