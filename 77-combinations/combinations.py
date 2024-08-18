class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def back(i, cur):
            if len(cur) == k:
                ans.append(cur.copy())
                return
            if i > n: return
            cur.append(i)
            back(i + 1, cur)
            cur.pop()
            back(i + 1, cur)
        back(1, [])
        return ans