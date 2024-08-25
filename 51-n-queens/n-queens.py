class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posdi, negdi = set(), set(), set()
        ans = []
        def backtrack(row, cur):
            if row == n:
                ans.append(cur.copy())
                return
            for col in range(n):
                pos, neg = row + col, row - col
                if col in cols or pos in posdi or neg in negdi:
                    continue
                cols.add(col)
                posdi.add(pos)
                negdi.add(neg)
                cur.append(("." * col) + 'Q' + ("." * (n - col - 1)))
                backtrack(row + 1, cur)
                cols.remove(col)
                posdi.remove(pos)
                negdi.remove(neg)
                cur.pop()
        backtrack(0, [])
        return ans