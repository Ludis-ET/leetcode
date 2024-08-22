class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        i = 0
        while num:
            if (num & 1) == 0:
                ans += 1 << i
            i += 1
            num >>= 1
        return ans