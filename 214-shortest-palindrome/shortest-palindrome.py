class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix, suffix = 0, 0
        base, mod = 29, 10**9 + 7
        last, power = 0, 1

        for i, c in enumerate(s):
            char = (ord(c) - ord('a') + 1)
            prefix = (prefix * base) % mod
            prefix = (prefix + char) % mod
            suffix = (suffix + char * power) % mod
            power = (power * base) % mod

            if prefix == suffix:
                last = i
        suffix = s[last + 1:]
        return suffix[::-1] + s