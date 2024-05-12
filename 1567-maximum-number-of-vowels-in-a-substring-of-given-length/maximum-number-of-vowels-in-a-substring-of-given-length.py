class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = {'a', 'e', 'i', 'o', 'u'}
        ans, l, v = 0, 0, 0
        for r in range(len(s)):
            v += 1 if s[r] in vow else 0
            if r - l + 1 > k:
                v -= 1 if s[l] in vow else 0
                l += 1
            ans = max(v, ans)
        return ans


                