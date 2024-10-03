class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        r = sum(nums) % p
        if r == 0:
            return 0

        ans = len(nums)
        cur =  0
        table = {0 : -1}
        for i, n in enumerate(nums):
            cur = (cur + n) % p
            pre = (cur - r + p) % p
            if pre in table:
                l = i - table[pre]
                ans = min(ans, l)
            table[cur] = i
        return -1 if ans == len(nums) else ans