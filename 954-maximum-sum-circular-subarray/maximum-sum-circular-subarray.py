class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax, gmin = nums[0], nums[0]
        maxcur, mincur = 0, 0
        for num in nums:
            maxcur = max(maxcur + num, num)
            gmax = max(gmax, maxcur)

            mincur = min(mincur + num, num)
            gmin = min(gmin, mincur)
        return max(gmax, sum(nums) - gmin) if gmax >= 0 else gmax