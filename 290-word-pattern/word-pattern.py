class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s2 = s.split()
        table = {}
        if len(pattern) != len(s2):
            return False
        for a in range(len(pattern)):
            if pattern[a] not in table:
                if s2[a] in table.values():
                    return False
                table[pattern[a]] = s2[a]
            else:
                if table[pattern[a]] != s2[a]:
                    return False
        return True
