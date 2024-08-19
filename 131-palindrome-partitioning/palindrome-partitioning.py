class Solution:
    def pal(self, s, l, r) -> bool:
        while l <= r and s[l] == s[r]:
            l += 1
            r -= 1
        return l > r
    
    def partition(self, s: str) -> List[List[str]]:
        ans, cur = [], []
        def back(i):
            if i >= len(s): 
                ans.append(cur.copy())
                return
            for j in range(i, len(s)):
                if self.pal(s, i, j):
                    cur.append(s[i: j + 1])
                    back(j + 1)
                    cur.pop()
        back(0)
        return ans