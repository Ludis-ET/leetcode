class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        table, check = defaultdict(set), set()
        for i, j in edges:
            table[i].add(j)
            table[j].add(i)

        def dfs(i):
            check.add(i)
            count, elements = len(table[i]), 1
            for j in table[i]:
                if j not in check:
                    c, e = dfs(j)
                    count += c
                    elements += e
            return [count, elements]
            
        ans = 0
        for i in range(n):
            if i not in check:
                c, e = dfs(i)
                c //= 2
                if c == (e * (e - 1)) // 2:
                    ans += 1
        return ans