class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c, count = 0, 0
        for a in nums:
            if a == 1:
                c += 1
            else:
                c = 0
            count = max(count,c)
        return count