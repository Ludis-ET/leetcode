class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rec(n, k):
            if k == 1:
                return 0
            ln = pow(2, n) - 1
            md = ceil(ln / 2)
            if k == md:
                return 1
            elif k < md:
                return rec(n - 1, k)
            else:
                return int(not rec(n - 1, 1 + (ln - k)))
        return str(rec(n, k))
