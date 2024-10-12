class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        def change(r, c):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != 'O':
                return
            board[r][c] = '#'
            change(r, c - 1)
            change(r, c + 1)
            change(r - 1, c)
            change(r + 1, c)

        rows, cols = len(board), len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                    change(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'