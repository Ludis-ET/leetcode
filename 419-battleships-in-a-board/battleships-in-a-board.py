class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        seen = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in seen or board[r][c] == '.':
                return
            seen.add((r, c))
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r + 1, c)
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and board[r][c] != '.':
                    ans += 1
                    dfs(r, c)
        return ans