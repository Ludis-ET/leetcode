class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False

        table1 = {}
        for a in range(len(s)):
            if s[a] not in table1:
                table1[s[a]] = t[a]
            else:
                if table1[s[a]] != t[a]:
                    return False
        if (len(table1) * 2) != (len(set(s)) + len(set(t))): return False
        return True
