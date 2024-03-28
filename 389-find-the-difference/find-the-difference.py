class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = b = 0
        for c, d in zip(s,t):
            a += ord(c)
            b += ord(d)
        b += ord(t[-1])
        
        return chr(b - a)