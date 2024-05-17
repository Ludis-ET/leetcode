class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        f = 0
        prefix = []
        for i in nums:
            prefix.append(f + i)
            f+=i
        return prefix