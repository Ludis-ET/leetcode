class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        l = 0
        for r in range(len(s)):            
            if r - l + 1 == 3:
                a, b, c = s[r], s[r - 1], s[r - 2]
                if a != b and a != c and b != c:
                    ans += 1
                l += 1
        return ans