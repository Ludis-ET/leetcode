class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        table = {}
        nums.sort()
        res = -1

        for num in nums:
            sqrt = isqrt(num)
            if sqrt * sqrt == num and sqrt in table:
                table[num] = table[sqrt] + 1
                res = max(res, table[num])
            else:
                table[num] = 1

        return res