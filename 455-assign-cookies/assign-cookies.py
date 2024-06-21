class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l= 0 
        ans = 0
        for i in g:
            while l < len(s) and i > s[l]:
                l += 1
            if l < len(s): ans += 1
            l += 1
        return ans

