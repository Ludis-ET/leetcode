class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = defaultdict(int)
        ans = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            table[s[r]] += 1
            maxf = max(maxf, table[s[r]])

            while (r - l + 1) - maxf > k:
                table[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans