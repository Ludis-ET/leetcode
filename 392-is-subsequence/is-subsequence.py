class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a, b = 0, 0
        while b < len(t) and a < len(s):
            if s[a] == t[b]:
                a += 1
            b += 1
        else: 
            return a == len(s)
        return False
