class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        table = defaultdict(int)
        table2 = defaultdict(int)
        for i in t:
            table[i] += 1

        have, need = 0, len(table)
        ans, ansL = [-1,-1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            table2[c] += 1

            if c in table and table2[c] == table[c]:
                have += 1

            while have == need:
                w = r - l + 1
                if w < ansL:
                    ans = [l, r]
                    ansL = w
                table2[s[l]] -= 1
                if s[l] in table and table2[s[l]] < table[s[l]]:
                    have -= 1
                l += 1
        l, r = ans
        return s[l: r + 1] if ansL != float('inf') else ''


