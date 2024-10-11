class Solution:
    def findCircleNum(self, con: List[List[int]]) -> int:
        checked = set()
        def dfs(i):
            checked.add(i)
            for j, el in enumerate(con[i]):
                if j not in checked and el == 1:
                    dfs(j)
        ans = 0
        for i in range(len(con)):
            if i not in checked:
                ans += 1
                dfs(i)
        return ans
            