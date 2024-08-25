class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        on, rows, cols, dig1, dig2 = set(), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        for r, c in lamps:
            if (r, c) not in on:
                on.add((r, c))
                rows[r] += 1
                cols[c] += 1
                dig1[r + c] += 1
                dig2[r - c] += 1
                
        ans = [0] * len(queries)
        for i, val in enumerate(queries):
            row, col = val
            if (rows[row] > 0) or (cols[col] > 0) or (dig1[row + col] > 0) or (dig2[row - col] > 0):
                ans[i] = 1
            ons = []
            if (row, col) in on: ons.append([row, col])
            if row - 1 >= 0 and col - 1 >= 0 and (row - 1, col - 1) in on: ons.append([row - 1, col - 1])
            if col - 1 >= 0 and (row, col - 1) in on: ons.append([row, col - 1])
            if row - 1 >= 0 and (row - 1, col) in on: ons.append([row - 1, col])
            if row + 1 < n and col + 1 < n and (row + 1, col + 1) in on: ons.append([row + 1, col + 1])
            if col + 1 < n and (row, col + 1) in on: ons.append([row, col + 1])
            if row + 1 < n and (row + 1, col) in on: ons.append([row + 1, col])
            if row + 1 < n and col - 1 >= 0 and (row + 1, col - 1) in on: ons.append([row + 1, col - 1])
            if row - 1 >= 0 and col + 1 < n and (row - 1, col + 1) in on: ons.append([row - 1, col + 1])
            for row, col in ons:
                rows[row] -= 1
                cols[col] -= 1
                dig1[row + col] -= 1
                dig2[row - col] -= 1
                on.remove((row, col))
        return ans




