class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        table1 = defaultdict(int)
        table2 = defaultdict(int)
        for i in range(len(p)):
            table1[p[i]] += 1
            table2[s[i]] += 1

        ans = [0] if table1 == table2 else []
        l = 0
        for r in range(len(p), len(s)):
            table2[s[r]] += 1
            table2[s[l]] -= 1
            if table2[s[l]] == 0: del table2[s[l]]
            l += 1

            if table1 == table2:
                ans.append(l)
        return ans

