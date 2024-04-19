class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        l, r = 0, k
        while l < len(s):
            ans += s[l:r][::-1]
            ans += s[r:r+k]
            l += 2 * k
            r += 2 * k
        return ans