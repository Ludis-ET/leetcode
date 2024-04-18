class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c**0.5)
        while l <= r:
            n = (l * l) + (r * r)
            if n == c:
                return True
            elif n < c:
                l += 1
            else:
                r -= 1
        return False
