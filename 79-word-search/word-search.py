class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def back(x, y, i):
            if i == len(word):
                return True
            if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != word[i]:
                return False

            temp = board[x][y]
            board[x][y] = '#'

            found = (back(x + 1, y, i + 1) or 
                     back(x - 1, y, i + 1) or 
                     back(x, y + 1, i + 1) or 
                     back(x, y - 1, i + 1))
            
            board[x][y] = temp
            return found
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and back(i, j, 0):
                    return True
        
        return False