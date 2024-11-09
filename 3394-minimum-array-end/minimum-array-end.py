class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        l, r = 0, 0
        while l < n.bit_length():
            if x & 1 << r == 0:
                if n & 1 << l != 0:
                    x |= 1 << r
                l += 1
            r += 1
        return x