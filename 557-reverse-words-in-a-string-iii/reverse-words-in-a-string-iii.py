class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        l = list(s.split())
        for i,a in enumerate(l):
            ans += a[::-1]
            if i != len(l) - 1: ans += " "
        return ans


