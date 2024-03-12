class Solution:
    def climbStairs(self, n: int) -> int:
        f = s = 1
        for a in range(n-1):
            temp = f
            f += s
            s = temp
        return f