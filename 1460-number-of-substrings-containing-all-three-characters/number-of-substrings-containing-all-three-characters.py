class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        table = defaultdict(int)
        ans, l = 0, 0
        for r in range(len(s)):
            table[s[r]] += 1

            while all(table[c] > 0 for c in 'abc'):
                ans += len(s) - r
                table[s[l]] -= 1
                l += 1
        return ans
