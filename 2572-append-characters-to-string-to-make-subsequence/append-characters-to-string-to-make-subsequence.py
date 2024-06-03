class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l, r = 0, 0
        while l < len(s) and r < len(t):
            if t[r] == s[l]:
                r += 1
            l += 1
        return len(t) - r